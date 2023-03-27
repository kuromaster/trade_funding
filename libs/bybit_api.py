import requests
import json
import traceback
import sys

import urllib3
import hashlib
import time
import hmac

from .vars import VarsInMemory
from .cprint import *

def get_tickerinfo(ticker:str, cur_timestamp: int):
    cprint("GREEN", "RUN get_tickerinfo")
    VarsInMemory.funding_nextrun = cur_timestamp + 1800
    if ticker not in VarsInMemory.ticker_info :
        VarsInMemory.ticker_info[ticker] = {'nextFundingTime': 0, 'bidPrice': 0, 'askPrice': 0, 'lastPrice': 0}
    
    if cur_timestamp > int(VarsInMemory.ticker_info[ticker]['nextFundingTime']):
        # url = ConfigVars.funding_url + ticker + 'USDT'
        url = VarsInMemory.funding_url
        response = requests.request("GET", url, headers=VarsInMemory.funding_headers, data=VarsInMemory.funding_payload)
        
        data_res = json.loads(response.text)
        
        for element in data_res['result']['list']:
            ticker_arr = element['symbol']
            try:
                if element['symbol'] not in VarsInMemory.funding_blacklist:
                    # if ticker_arr == ticker:
                        # cprint('GREEN', json.dumps(element, indent=2))
                        # pass
                    VarsInMemory.ticker_info[ticker_arr] = {'nextFundingTime': 0, 'bidPrice': 0, 'askPrice': 0, 'lastPrice': 0}
                    VarsInMemory.ticker_info[ticker_arr]['nextFundingTime'] = int(element["nextFundingTime"][:-3])
                    VarsInMemory.ticker_info[ticker_arr]['bidPrice'] = element["bidPrice"]
                    VarsInMemory.ticker_info[ticker_arr]['askPrice'] = element["askPrice"]
                    VarsInMemory.ticker_info[ticker_arr]['lastPrice'] = element["lastPrice"]
                    
                    # VarsInMemory.ticker_info[ticker_arr]['time_sell'] = VarsInMemory.ticker_info[ticker_arr]['nextFundingTime'] - VarsInMemory.funding_delta
            except:
                if VarsInMemory.debug_on_except:
                    msg = "[ERROR] {}".format(sys.exc_info()[1])
                    cprint("RED", msg)
                    cprint("YELLOW", 'ticker(not edited): {}'.format(element['symbol']))
                    # cprint("YELLOW", 'ticker: {}'.format(ticker_arr))
                    # cprint("YELLOW", 'nextFundingTime: {}'.format(element['nextFundingTime'][:-3]))
                    print(traceback.format_exc())
                    break
                pass
    
    cprint('BLUE', json.dumps(VarsInMemory.ticker_info[ticker], indent=2))


def get_open_orders(ticker:str, category: str = 'linear' ):
    cprint("GREEN", "RUN get_open_orders")
    query_str = f'category={category}&symbol={ticker}'

    url = f'https://api.bybit.com/v5/order/realtime?{query_str}'
    ts = str(round(time.time() * 1000))
    recv_window = str(5000)
    
    # Create the param str    
    param_str = ts+VarsInMemory.API_KEY+recv_window+query_str
    
    # Generate the signature
    hash = hmac.new(
        bytes(VarsInMemory.API_SECRET, "utf-8"),
        param_str.encode("utf-8"),
        hashlib.sha256
    )
    
    signature = hash.hexdigest()
    # cprint("PURPLE", f'sign: {signature}')

    urllib3.disable_warnings()
    
    payload = {}
    headers = {
        'X-BAPI-API-KEY': VarsInMemory.API_KEY,
        'X-BAPI-TIMESTAMP': ts,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': str(signature)
    }
    
    # cprint("BLUE", f'HEADERS: {headers}')
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data_res = json.loads(response.text)
    
    # print(response)
    cprint('GREEN', f'HTTP CODE: {response.status_code}')
    cprint('BLUE', json.dumps(data_res, indent=2))


def place_order(ticker: str, size: str, side: str = None, price: str = None, category: str = 'linear'):
    cprint("GREEN", "RUN place_order")
    ts = str(round(time.time() * 1000))
    recv_window = str(5000)
    # if side is None:
    #     side = 'Sell'
    orderLinkId = f'funding_{side}_{ticker}_{ts}'
    if price is None:
        query_str = f'category={category}&symbol={ticker}&side={side}&orderType=Market&qty={size}&orderLinkId={orderLinkId}'
    else:
        query_str = f'category={category}&symbol={ticker}&side={side}&orderType=Market&qty={size}&orderLinkId={orderLinkId}&price={price}'
        
    url = f'https://api.bybit.com/v5/order/realtime?{query_str}'
    
    
    # Create the param str    
    param_str = ts+VarsInMemory.API_KEY+recv_window+query_str
    
    # Generate the signature
    hash = hmac.new(
        bytes(VarsInMemory.API_SECRET, "utf-8"),
        param_str.encode("utf-8"),
        hashlib.sha256
    )
    
    signature = hash.hexdigest()

    urllib3.disable_warnings()
    
    payload = {}
    headers = {
        'X-BAPI-API-KEY': VarsInMemory.API_KEY,
        'X-BAPI-TIMESTAMP': ts,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': str(signature)
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data_res = json.loads(response.text)
    
    if ticker in VarsInMemory.order_info:
        VarsInMemory.order_info[ticker].append({"orderId": data_res['result']['orderId'],"orderLinkId": data_res['result']['orderLinkId']})
    else:
        VarsInMemory.order_info[ticker] = {"orderId": data_res['result']['orderId'],"orderLinkId": data_res['result']['orderLinkId']}
    
    
    # print(response)
    cprint('BLUE', f'HTTP CODE: {response.status_code}')
    # print(data_res)
    cprint('BLUE', json.dumps(data_res, indent=2))


def get_tickers(ticker: str = None, category: str = 'linear'):
    cprint("GREEN", "RUN get_tickers")
    if ticker is None:
        query_str = f'category={category}'
    else:
        query_str = f'category={category}&symbol={ticker}'

    url = f'https://api.bybit.com/v5/market/tickers?{query_str}'
    ts = str(round(time.time() * 1000))
    recv_window = str(5000)
    
    # Create the param str    
    param_str = ts+VarsInMemory.API_KEY+recv_window+query_str
    
    # Generate the signature
    hash = hmac.new(
        bytes(VarsInMemory.API_SECRET, "utf-8"),
        param_str.encode("utf-8"),
        hashlib.sha256
    )
    
    signature = hash.hexdigest()
    # cprint("PURPLE", f'sign: {signature}')

    urllib3.disable_warnings()
    
    payload = {}
    headers = {
        'X-BAPI-API-KEY': VarsInMemory.API_KEY,
        'X-BAPI-TIMESTAMP': ts,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': str(signature)
    }
    
    # cprint("BLUE", f'HEADERS: {headers}')
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data_res = json.loads(response.text)
    
    # print(response)
    cprint('GREEN', f'HTTP CODE: {response.status_code}')
    cprint('BLUE', json.dumps(data_res, indent=2))
    if ticker is not None:
        VarsInMemory.ticker_info[ticker] = {'nextFundingTime': 0, 'bidPrice': 0, 'askPrice': 0, 'lastPrice': 0}
        VarsInMemory.ticker_info[ticker]['nextFundingTime'] = int(data_res['result']['list'][0]["nextFundingTime"][:-3])
        VarsInMemory.ticker_info[ticker]['bidPrice'] = data_res['result']['list'][0]["bid1Price"]
        VarsInMemory.ticker_info[ticker]['askPrice'] = data_res['result']['list'][0]["ask1Price"]
        VarsInMemory.ticker_info[ticker]['lastPrice'] = data_res['result']['list'][0]["lastPrice"]
        cprint('CYAN', json.dumps(VarsInMemory.ticker_info[ticker], indent=2))
    
    
def cancel_order(ticker: str, category: str = 'linear'):
    cprint("GREEN", "RUN cancel_order")
    if ticker is None:
        query_str = f'category={category}'
    else:
        query_str = f'category={category}&symbol={ticker}'

    url = f'https://api.bybit.com/v5/order/cancel?{query_str}'
    ts = str(round(time.time() * 1000))
    recv_window = str(5000)
    
    # Create the param str    
    param_str = ts+VarsInMemory.API_KEY+recv_window+query_str
    
    # Generate the signature
    hash = hmac.new(
        bytes(VarsInMemory.API_SECRET, "utf-8"),
        param_str.encode("utf-8"),
        hashlib.sha256
    )
    
    signature = hash.hexdigest()
    # cprint("PURPLE", f'sign: {signature}')

    urllib3.disable_warnings()
    
    payload = {}
    headers = {
        'X-BAPI-API-KEY': VarsInMemory.API_KEY,
        'X-BAPI-TIMESTAMP': ts,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': str(signature)
    }
    
    # cprint("BLUE", f'HEADERS: {headers}')
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data_res = json.loads(response.text)
    
    # print(response)
    cprint('GREEN', f'HTTP CODE: {response.status_code}')
    cprint('BLUE', json.dumps(data_res, indent=2))


def get_history(orderLinkId: str = None, category: str = 'linear'):
    cprint("GREEN", "RUN get_history")
    if orderLinkId is None:
        query_str = f'category={category}'
    else:
        query_str = f'category={category}&orderLinkId={orderLinkId}'

    url = f'https://api.bybit.com/v5/order/history?{query_str}'
    ts = str(round(time.time() * 1000))
    recv_window = str(5000)
    
    # Create the param str    
    param_str = ts+VarsInMemory.API_KEY+recv_window+query_str
    
    # Generate the signature
    hash = hmac.new(
        bytes(VarsInMemory.API_SECRET, "utf-8"),
        param_str.encode("utf-8"),
        hashlib.sha256
    )
    
    signature = hash.hexdigest()
    # cprint("PURPLE", f'sign: {signature}')

    urllib3.disable_warnings()
    
    payload = {}
    headers = {
        'X-BAPI-API-KEY': VarsInMemory.API_KEY,
        'X-BAPI-TIMESTAMP': ts,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': str(signature)
    }
    
    # cprint("BLUE", f'HEADERS: {headers}')
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data_res = json.loads(response.text)
    
    # print(response)
    cprint('GREEN', f'HTTP CODE: {response.status_code}')
    cprint('PURPLE', json.dumps(data_res, indent=2))
