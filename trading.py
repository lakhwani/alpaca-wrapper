import requests, json
from datetime import date, timedelta

#---------INSERT API KEY & SECRET KEY

API_KEY = " - "
SECRET_KEY = " - "

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADER = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

#---------ACESSING ACCOUNT DATA

#access acount data (id, portfolio value, buying power, etc.)
def getAccount():
    r = requests.get(ACCOUNT_URL, headers=HEADER)
    info = json.loads(r.content)
    return info

#---------CREATING BUY/SELL ORDERS

#create a market or stop order                       
def createOrder(symbol, qty, notional, side, order_type, time_in_force, 
                limit_price, stop_price, trail_price, trail_percent): 
    #time_in_force => (day -> day order, gtc -> good till cancelled)
    data = {
        "symbol": symbol,
        "qty": qty,
        "notional": notional,
        "side": side,
        "type": order_type,
        "time_in_force": time_in_force,
        "limit_price": limit_price,
        "stop_price": stop_price,
        "trail_price": trail_price,
        "trail_percent": trail_percent,
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADER)
    return json.loads(r.content)

#---------ACCESSING ORDER HISTORY

#return list of open orders (not filled yet)
def getOrders():
    r = requests.get(ORDERS_URL, headers=HEADER)
    return json.loads(r.content)

#return list of all orders (from past n hours) of stock symbols [eg: (MSFT, )]
def getOrderSpec(n, stock_symbols):
    currentTime = date.now()
    prevTime = date.now() - timedelta(hours=n)
    data = {
        "status": "all",
        "limit": "50",
        "after": "{}".format(prevTime),
        "until": "{}".format(currentTime),
        "direction": "desc",
        "nested": "True",
        "symbols": stock_symbols,
    }
    r = requests.get(ORDERS_URL, json=data, headers=HEADER)
    return json.loads(r.content)

#---------ORDER PATCHING & ORDER CANCELLATION

def modifyOrder(order_id, qty, time_in_force, limit_price, stop_price, tail):
    ORDERS_URL_id = "{}/v2/orders/{}".format(BASE_URL, order_id)
    data = {
        "qty": qty,
        "time_in_force": time_in_force,
        "limit_price": limit_price,
        "stop_price": stop_price,
        "tail": tail
    }
    r = requests.delete(ORDERS_URL_id, json=data, headers=HEADER)
    return json.loads(r.content)

def cancelOrder(order_id):
    ORDERS_URL_id = "{}/v2/orders/{}".format(BASE_URL, order_id)
    r = requests.delete(ORDERS_URL_id, headers=HEADER)
    return json.loads(r.content)

def cancelAll():
    r = requests.delete(ORDERS_URL, headers=HEADER)
    return json.loads(r.content) 

#---------------------------------------------
