from dotenv import load_dotenv
import requests
import pandas as pd
import os
from datetime import datetime, timedelta

# Load environment variables from .env file
load_dotenv() 
'''
If load_dotenv() doesn't work then do this:
load_dotenv('C:/Users/Your Name/Downloads/Github Projects/Currency_converter/.env'). 
Here, Replace .env with .env_sample
'''

# Get the API key from the environment
app_id = os.getenv('OPEN_EXCHANGE_API_KEY')

if app_id is None:
    print("Error: API key not found. Please check your .env file.")
else:
    print("API key loaded successfully.")


# Get the current year and month
current_date = datetime.now()
year = current_date.year
month = (current_date.month) - 1

# If the current month is January, we need to go to December of the previous year
if month == 0:
    month = 12
    year -= 1

# Find the first day of the previous month
first_day_of_previous_month = datetime(year=year, month=month, day=1)
# Format the first day of the previous month as DD/MM/YYYY
formatted_first_day_of_previous_month = first_day_of_previous_month.strftime('%Y-%m-%d')

# Find the last day of the previous month
first_day_of_current_month = datetime(year=current_date.year, month=current_date.month, day=1)
last_date_of_previous_month = first_day_of_current_month - timedelta(days=1)
last_date_str = last_date_of_previous_month.strftime('%Y-%m-%d')


# Function to get exchange rates and convert to GBP
def get_exchange_rates_to_gbp(formatted_date, last_date, app_id):
    '''
    Defines a function to fetch exchange rates and convert them to GBP. It takes:
        formatted_date: Start of the previous month (used for table labeling).
        last_date: End of the previous month (used for API requests).
        app_id: The API key for authenticating with the Open Exchange Rates service.
    '''

    url = f'https://openexchangerates.org/api/historical/{last_date}.json'
    params = { 
        'app_id': app_id   #Contains the API key as a parameter for authentication.
    }
    
    # Make a GET request to the Open Exchange Rates API
    response = requests.get(url, params=params)  # Sends a GET request to the API with the specified parameters.

    if response.status_code == 200: #Checks if the API request was successful 
        data = response.json() #Parses the JSON response into a Python dictionary
    
       
        # Get the USD to GBP rate
        if 'GBP' in data['rates']:
            usd_to_gbp = data['rates']['GBP']
            
            # List of currencies to convert to GBP
            currencies = ['USD', 'INR', 'AUD', 'PLN', 'EUR', 'CAD']
            exchange_data = []
            
            for currency in currencies:
                if currency in data['rates']:
                    rate_in_usd = data['rates'][currency]
                    if currency == 'USD':
                        rate_in_gbp = usd_to_gbp  # USD to GBP is already in the data
                    else:
                        rate_in_gbp = usd_to_gbp / rate_in_usd  # Corrected calculation
                    
                    # Append the data to the list
                    exchange_data.append({
                        'Start of Month': formatted_date,
                        'Currency code': currency,
                        'GBP': round(rate_in_gbp, 6)
                    })
                    
            # Create a DataFrame from the collected data
            df = pd.DataFrame(exchange_data)
            return df
        else:
            print(f"GBP rate not available for {last_date}")
    elif response.status_code == 403:  # Handle 403 Forbidden error
        print("Access forbidden: Please check your API key or subscription plan.")
        return None 
    else:
        print(f"Failed to fetch data for {last_date}. Status code: {response.status_code}")
        return None

# Example usage
df = get_exchange_rates_to_gbp(formatted_first_day_of_previous_month, last_date_str, app_id)

# Reorder columns and display the DataFrame
if df is not None and not df.empty:
    df = df.reindex(['Start of Month', 'GBP', 'Currency code'], axis=1)
    print(df)