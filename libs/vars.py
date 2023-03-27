from dotenv import load_dotenv
import os

load_dotenv()

class VarsInMemory:
    
    app_dir = "/opt/funding"
    
    debug_on_cprint = True
    debug_on_except = True
    
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    
    #####################
    ### bybbit_api.py ###
    #####################
    ticker = 'COTIUSDT'
    
    # Переменные для получение последних данных по тикерам
    funding_url = 'https://api.bybit.com/derivatives/v3/public/tickers'
    funding_payload={}
    funding_headers = {}
    
    # Timestamp следующего запроса funding time
    funding_nextrun = 0
    # Интервал следующего запроса funding time. В секундах.
    funding_nextrun_sleep = 1800
    
    # BLACK LIST TICKER для избежания ошибок при получении funding time
    funding_blacklist = ['BTC-07APR23', 'BTC-24MAR23', 'BTC-26MAY23', 'BTC-28APR23', 'BTC-29SEP23', 'BTC-30JUN23', 'BTC-31MAR23', 'BTCUSDH23', 'BTCUSDM23', 'BTCUSDU23', 'ETH-07APR23', 'ETH-24MAR23', 'ETH-26MAY23', 'ETH-28APR23', 'ETH-29SEP23', 'ETH-30JUN23', 'ETH-31MAR23', 'ETHUSDH23', 'ETHUSDM23', 'ETHUSDU23', 'BTC-14APR23', '-']
    
    # Здесь хранится вся инфа, которую мы получаем в запросе - время следущего фандинга, текущая цена и т.д.
    # symbol, bidPrice, askPrice, lastPrice, lastTickDirection, prevPrice24h, price24hPcnt, highPrice24h, lowPrice24h, prevPrice1h, markPrice, indexPrice, openInterest, turnover24h, volume24h, fundingRate, nextFundingTime, predictedDeliveryPrice, basisRate, deliveryFeeRate, deliveryTime
    ticker_info = {}
    order_info = {}
    
    while_flag = True
    delta_price = 0.8
