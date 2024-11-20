import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_btc_data(input_csv, output_csv):
    """
    Load, preprocess, and engineer features for BTC data.
    """
    # Load raw data
    btc_data = pd.read_csv(input_csv, index_col='timestamp', parse_dates=True)

    # Add features
    btc_data['daily_return'] = btc_data['close'].pct_change()
    btc_data['ma_7'] = btc_data['close'].rolling(window=7).mean()
    btc_data['ma_30'] = btc_data['close'].rolling(window=30).mean()
    btc_data['volatility_7'] = btc_data['close'].rolling(window=7).std()
    
    # Handle missing values
    btc_data.fillna(method='ffill', inplace=True)

    # Normalize data
    scaler = MinMaxScaler()
    btc_data[['close', 'volume']] = scaler.fit_transform(btc_data[['close', 'volume']])

    # Save processed data
    btc_data.to_csv(output_csv)
    print(f"Processed data saved to {output_csv}")
