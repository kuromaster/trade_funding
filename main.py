#! /opt/funding/venv/bin/python3

import time
from libs.bybit_api import *
from libs.vars import VarsInMemory


def main():
    cur_timestamp = int(time.time())
    # get_tickerinfo(VarsInMemory.ticker, cur_timestamp)
    get_open_orders(ticker=VarsInMemory.ticker)
    get_tickers(ticker=VarsInMemory.ticker)
    # cancel_order(ticker=VarsInMemory.ticker )
    # while VarsInMemory.while_flag:
    #     if cur_timestamp >= (VarsInMemory.ticker_info[VarsInMemory.ticker]['nextFundingTime'] - 5):
    #         place_order(ticker=VarsInMemory.ticker, size='1', side='Sell')
    #         get_history(orderLinkId=VarsInMemory.order_info[VarsInMemory.ticker]['orderLinkId'])
    #         # Переделать поиск цены
    #         get_tickers(ticker=VarsInMemory.ticker)
    #         time.sleep(1)
            
    #         sell_price = int(VarsInMemory.ticker_info[VarsInMemory.ticker]['lastPrice']) - int(VarsInMemory.ticker_info[VarsInMemory.ticker]['lastPrice'])*VarsInMemory.delta_price
    #         get_history(orderLinkId=VarsInMemory.order_info[VarsInMemory.ticker]['orderLinkId'])
    #         place_order(ticker=VarsInMemory.ticker, size='1', side='Buy', price=str(sell_price))
    #         cur_timestamp = int(time.time())
            
    #         while cur_timestamp < VarsInMemory.ticker_info[VarsInMemory.ticker]['nextFundingTime']:
    #             time.sleep(0.5)
    #             cur_timestamp = int(time.time())

    #         get_tickers(ticker=VarsInMemory.ticker)
    #         get_history(orderLinkId=VarsInMemory.order_info[VarsInMemory.ticker]['orderLinkId'])
            
    #     time.sleep(0.5)
    #     cur_timestamp = int(time.time())

if __name__ == '__main__':
    main()
