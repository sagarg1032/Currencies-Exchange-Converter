# Currency Exchange Converter

This script fetches historical currency exchange rates for the previous month and converts specified currencies to GBP using data from the Open Exchange Rates API. It automates the process of determining the relevant dates, fetching data, and structuring it in a user-friendly format.


## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup and Usage](#setup-and-usage)
4. [How It Works](#how-it-works)
5. [Example Input](#example-input)
6. [Example Output](#example-output)
7. [Error Handling](#error-handling)
8. [Notes](#notes)
9. [Contributions](#contributions)
10. [License](#license)
11. [Author](#author)
12. [Feedback](#feedback)


## Features
- Automatically calculates the start and end dates of the previous month for accurate historical data retrieval.
- Fetches and processes historical exchange rates from the Open Exchange Rates API.
- Converts specified currencies to GBP and structures the output in a tabular format (Pandas DataFrame).
- Provides flexibility to export the DataFrame to CSV or Excel for reporting purposes.


## Prerequisites
- Python 3.7 or higher
- Required Python packages:
  - `requests`
  - `pandas`
- Check Documentation for more reference: [Open Exchange Rates API](https://docs.openexchangerates.org/reference/api-introduction)

### Configure the `.env` file
To avoid hardcoding sensitive information like the API key, create a `.env` file and type:

```bash
OPEN_EXCHANGE_API_KEY='your_api_key' 
```
Note: *Replace your_api_key with your actual API key.*


In your Python script, access the API key as:
```python
import os
# Get the API key from the environment
app_id = os.getenv('OPEN_EXCHANGE_API_KEY')

if app_id is None:
    print("Error: API key not found. Please check your .env file.")
else:
    print("API key loaded successfully.")
```

## Setup

### Sign up with Open exchange Rates
- Sign up by making a new account with Open Exchange Rates
- Choose a plan that suits your requirements (note that some features, like historical data, may work with a free plan, but there is a cap of 1000 requests per month)
- Navigate to Integration > API ID, create a new API name, and generate an API ID (this is your API key).
- Refer to Usage Statistics on the dashboard to monitor your monthly request allowance and incurred costs. 

### Clone the repo
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```

### Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### Run the Script
Run the script to fetch exchange rates:
```bash
python currency_exchange_converter.py
```


## How It Works
1. **Calculate Dates**: The script calculates the first and last dates of the previous month using Python's `datetime` module.
2. **Fetch Exchange Rates**: Sends a GET request to the Open Exchange Rates API to retrieve historical exchange rate data.
3. **Convert to GBP**: Processes the API response to convert specified currency rates into GBP.
4. **Output Data**: Outputs the processed data into a Pandas DataFrame with columns for date, GBP rate, and currency code.

## Example Input
No direct input is required. The script automatically calculates the relevant dates and fetches data based on those.

## Example Output
The script outputs a DataFrame with the following format:
```
  Start of Month       GBP Currency code
0     2023-11-01  0.770123           USD
1     2023-11-01  0.011234           INR
2     2023-11-01  0.550456           AUD
...
```

## Error Handling
- If the API key is invalid or the API is unreachable, the script prints an error message.
- If the GBP rate is unavailable, the script notifies the user.
- Includes basic exception handling for network and JSON parsing errors.

## Notes
- Ensure your Open Exchange Rates API plan supports historical data retrieval
- The script is designed to be easily extended for additional currencies or features
- Verify that your .env file is properly configured and the API key is valid before running the script
- If you face issues with 403 Forbidden errors, check:
  - Your API key's validity
  - Your subscription plan's support for the requested API features (e.g., historical data)
  - Monthly request limits in your account dashboard
- To learn more about how the script processes and converts currencies, refer to the [currency_conversion_example.md](./currency_conversion_example.md) file, else directly jump to the main script i.e. [currency_exchange_converter.py](./currency_exchange_converter.py)


## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- **Sagar Gupta**
- GitHub: [sagarg1032](https://github.com/sagarg1032) - Explore more projects and contributions.

## Feedback
If you have any feedback or suggestions, feel free to open an issue or contact me directly.