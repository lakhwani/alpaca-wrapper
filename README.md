# Alpaca Trading Python Wrapper (`trader.py`)

## Overview
`trader.py` is a Python wrapper for the Alpaca Trading API, designed for automating trading activities on the Alpaca platform. This script facilitates various trading operations including accessing account data, creating and managing orders, and handling order cancellations.

## Features
- **Account Data Access**: Retrieves details like account ID, portfolio value, and buying power.
- **Order Management**: Supports creating market or stop orders with various parameters.
- **Order History**: Retrieves open orders and past orders based on specified criteria.
- **Order Modification and Cancellation**: Allows users to modify or cancel existing orders, as well as cancel all open orders.

## Requirements
- Python 3.x
- Alpaca API Key and Secret Key
- Requests library

## Installation
1. Clone or download the script:
2. Install the `requests` library:
   ```
   pip install requests
   ```

## Setup
Insert your Alpaca API Key and Secret Key in the `trader.py` script:
```python
API_KEY = "your_api_key_here"
SECRET_KEY = "your_secret_key_here"
```

## Usage
Import and use the functions in the `trader.py` script in your Python environment. Examples of function usage:

```python
from trader import getAccount, createOrder, getOrders

# Access account data
account_data = getAccount()

# Create a buy order
order = createOrder("AAPL", 10, None, "buy", "market", "gtc", None, None, None, None)

# Get a list of open orders
open_orders = getOrders()
```

## Contributing
Contributions are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

## Disclaimer
This wrapper is provided as a tool to interact with the Alpaca API. It is not intended for use as financial advice. Trading involves risks, and users should conduct their own research and consult with financial experts before engaging in trading activities.
