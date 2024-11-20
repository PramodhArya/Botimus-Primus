from binance.client import Client
import pandas as pd
from datetime import datetime

def fetch_btc_data(api_key, api_secret, start_date, end_date):
    """
    Fetch historical BTC-USD data using Binance API.
    """
    # Initialize Binance client
    client = Client(api_key, api_secret, tld='us')  # Use Binance.US domain
    
    # Convert date strings to milliseconds
    start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp() * 1000)
    end_timestamp = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp() * 1000)
    
    # Fetch Klines (candlestick) data
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, start_timestamp, end_timestamp)
    
    # Convert to DataFrame
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 
               'quote_asset_volume', 'number_of_trades', 'taker_buy_base', 'taker_buy_quote', 'ignore']
    df = pd.DataFrame(klines, columns=columns)
    
    # Format data
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
    numeric_columns = ['open', 'high', 'low', 'close', 'volume', 'quote_asset_volume', 
                       'taker_buy_base', 'taker_buy_quote']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)
    
    # Set timestamp as index
    df.set_index('timestamp', inplace=True)
    return df[['open', 'high', 'low', 'close', 'volume']]

