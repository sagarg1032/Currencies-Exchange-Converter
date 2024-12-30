# How API Fetches Data and Performs Conversion

## Code Explanation
The code below demonstrates how to fetch exchange rate data from the Open Exchange Rates API for a specific date and calculate the GBP equivalent for one currency like INR. Similarly, you can use this code you get to get the GBP equivalent for different currencies.

```python
import requests
import os
from dotenv import load_dotenv


# Define the date for fetching historical exchange rates
last_date = '2024-12-29'
url = f'https://openexchangerates.org/api/historical/{last_date}.json'

# Load environment variables from .env file
load_dotenv() 
'''
If load_dotenv() doesn't work then do this:
load_dotenv('C:/Users/Your Name/Downloads/Github Projects/Currency_converter/.env'). Here, Replace .env with .env_sample
'''

# Get the API key from the environment
app_id = os.getenv('OPEN_EXCHANGE_API_KEY')
print("API Key:", app_id)

if app_id is None:
    print("Error: API key not found. Please check your .env file.")
else:
    print("API key loaded successfully.")


params = {
    'app_id': app_id
}

# Make a GET request to the Open Exchange Rates API
response = requests.get(url, params=params)  # Sends a GET request to the API with the specified parameters.

if response.status_code == 200:  # Checks if the API request was successful
    data = response.json()  # Parses the JSON response into a Python dictionary
    
    # Print the entire JSON response for debugging
    print("API Response Data:", data)
    
    # Get the USD to GBP rate
    if 'GBP' in data['rates']:
        usd_to_gbp = data['rates']['GBP']
        print("\n")
        print(f"USD to GBP Rate: {usd_to_gbp}")
    else:
        print("GBP rate is not available in the response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response Text:", response.text)
```

---


### Example Output:
```plaintext
API Response Data: {'disclaimer': 'Usage subject to terms: https://openexchangerates.org/terms', 'license': 'https://openexchangerates.org/license', 'timestamp': 1735516798, 'base': 'USD', 'rates': {'AED': 3.672993, 'AFN': 70.483864, 'ALL': 94.154318, 'AMD': 399.044309, 'ANG': 1.804345, 'AOA': 912, 'ARS': 1029.893727, 'AUD': 1.606439, 'AWG': 1.8, 'AZN': 1.7, 'BAM': 1.875797, 'BBD': 2, 'BDT': 119.666246, 'BGN': 1.876133, 'BHD': 0.377452, 'BIF': 2960.624136, 'BMD': 1, 'BND': 1.360284, 'BOB': 6.917949, 'BRL': 6.196004, 'BSD': 1, 'BTC': 1.0692958e-05, 'BTN': 85.655781, 'BWP': 13.925095, 'BYN': 3.276459, 'BZD': 2.011126, 'CAD': 1.440305, 'CDF': 2848.433737, 'CHF': 0.901883, 'CLF': 0.035968, 'CLP': 991.447179, 'CNH': 7.3018, 'CNY': 7.2988, 'COP': 4397.093429, 'CRC': 507.935663, 'CUC': 1, 'CUP': 25.75, 'CVE': 105.754568, 'CZK': 24.168, 'DJF': 178.286135, 'DKK': 7.151525, 'DOP': 60.892913, 'DZD': 135.55545, 'EGP': 50.842794, 'ERN': 15, 'ETB': 127.756654, 'EUR': 0.958819, 'FJD': 2.3224, 'FKP': 0.795041, 'GBP': 0.795041, 'GEL': 2.806, 'GGP': 0.795041, 'GHS': 14.717307, 'GIP': 0.795041, 'GMD': 71.9956, 'GNF': 8654.003353, 'GTQ': 7.718794, 'GYD': 209.370302, 'HKD': 7.76405, 'HNL': 25.438066, 'HRK': 7.224396, 'HTG': 130.906824, 'HUF': 394.73042, 'IDR': 16192.773907, 'ILS': 3.684266, 'IMP': 0.795041, 'INR': 85.386496, 'IQD': 1311.561885, 'IRR': 42250, 'ISK': 139.164615, 'JEP': 0.795041, 'JMD': 155.84328, 'JOD': 0.7091, 'JPY': 157.894, 'KES': 129.450205, 'KGS': 87, 'KHR': 4021.491937, 'KMF': 471.719457, 'KPW': 900, 'KRW': 1473.796586, 'KWD': 0.308445, 'KYD': 0.834316, 'KZT': 524.068491, 'LAK': 21884.539363, 'LBP': 89676.3055, 'LKR': 292.859531, 'LRD': 182.218385, 'LSL': 18.755383, 'LYD': 4.923033, 'MAD': 10.101472, 'MDL': 18.409948, 'MGA': 4696.758844, 'MKD': 59.0083, 'MMK': 2098, 'MNT': 3398, 'MOP': 8.004412, 'MRU': 39.937659, 'MUR': 46.949997, 'MVR': 15.4, 'MWK': 1736.05715, 'MXN': 20.323773, 'MYR': 4.4715, 'MZN': 63.830001, 'NAD': 18.755383, 'NGN': 1549.527379, 'NIO': 36.848416, 'NOK': 11.351664, 'NPR': 137.048871, 'NZD': 1.773348, 'OMR': 0.384913, 'PAB': 1, 'PEN': 3.746512, 'PGK': 4.006138, 'PHP': 57.899417, 'PKR': 278.705477, 'PLN': 4.095378, 'PYG': 7784.056779, 'QAR': 3.64878, 'RON': 4.7731, 'RSD': 112.146915, 'RUB': 105.470046, 'RWF': 1381.9594, 'SAR': 3.7553, 'SBD': 8.38356, 'SCR': 13.941399, 'SDG': 601.5, 'SEK': 10.99817, 'SGD': 1.35798, 'SHP': 0.795041, 'SLL': 20969.5, 'SOS': 572.195845, 'SRD': 35.08, 'SSP': 130.26, 'STD': 22281.8, 'STN': 23.497818, 'SVC': 8.76037, 'SYP': 13002, 'SZL': 18.748382, 'THB': 34.060281, 'TJS': 10.937994, 'TMT': 3.51, 'TND': 3.195032, 'TOP': 2.39453, 'TRY': 35.230469, 'TTD': 6.803817, 'TWD': 32.829, 'TZS': 2427.844759, 'UAH': 42.015247, 'UGX': 3672.380504, 'USD': 1, 'UYU': 44.099171, 'UZS': 12936.482705, 'VES': 51.701112, 'VND': 25455.011984, 'VUV': 118.722, 'WST': 2.8, 'XAF': 628.943862, 'XAG': 0.03396025, 'XAU': 0.00038105, 'XCD': 2.70255, 'XDR': 0.767755, 'XOF': 628.943862, 'XPD': 0.00109654, 'XPF': 114.41751, 'XPT': 0.0010815, 'YER': 249.852173, 'ZAR': 18.689375, 'ZMW': 27.758117, 'ZWL': 322}}


USD to GBP Rate: 0.795041
```

---

## Example of Conversion Calculation

### Example:
- **USD to GBP Rate**: 0.795041 (fetched from API)
- **Exchange Rate for INR to USD**: 85.386496

### Formula:
To calculate the conversion rate from INR to GBP:

\[
Rate in GBP = USD to GBP Rate\Exchange Rate for INR to USD
\]

### Calculation:
\[
Rate in GBP = 0.795041\85.386496
\]

### Result:
1 INR ≈ 0.00931 GBP