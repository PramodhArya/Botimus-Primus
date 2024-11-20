from btc_data_fetcher import fetch_btc_data
from btc_preprocessor import preprocess_btc_data
from datetime import datetime

# Configuration
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
START_DATE = "2019-01-01"
END_DATE = datetime.now().strftime("%Y-%m-%d")
RAW_DATA_FILE = "btc_binance_data.csv"
PROCESSED_DATA_FILE = "btc_processed_data.csv"

def main():
    # Fetch raw data
    print("Fetching BTC data...")
    btc_data = fetch_btc_data(API_KEY, API_SECRET, START_DATE, END_DATE)
    btc_data.to_csv(RAW_DATA_FILE)
    print(f"Raw data saved to {RAW_DATA_FILE}")

    # Preprocess data
    print("Preprocessing BTC data...")
    preprocess_btc_data(RAW_DATA_FILE, PROCESSED_DATA_FILE)

if __name__ == "__main__":
    main()
