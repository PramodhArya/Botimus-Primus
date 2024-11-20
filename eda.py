import pandas as pd
import matplotlib.pyplot as plt

def perform_eda(input_csv):
    """
    Perform exploratory data analysis on BTC data.
    """
    # Load processed data
    btc_data = pd.read_csv(input_csv, index_col="timestamp", parse_dates=True)

    # 1. Summary Statistics
    print("Summary Statistics:")
    print(btc_data.describe())

    # 2. Visualize Historical Prices
    plt.figure(figsize=(12, 6))
    plt.plot(btc_data['close'], label="Closing Price", alpha=0.7)
    plt.plot(btc_data['ma_7'], label="7-Day Moving Average", alpha=0.7)
    plt.plot(btc_data['ma_30'], label="30-Day Moving Average", alpha=0.7)
    plt.title("BTC Closing Prices and Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (Normalized)")
    plt.legend()
    plt.show()

    # 3. Analyze Returns
    plt.figure(figsize=(12, 6))
    plt.plot(btc_data['daily_return'], label="Daily Returns", alpha=0.7)
    plt.title("BTC Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Return")
    plt.legend()
    plt.show()

    # Histogram of returns
    plt.figure(figsize=(8, 6))
    plt.hist(btc_data['daily_return'].dropna(), bins=50, alpha=0.7, color='blue')
    plt.title("Distribution of BTC Daily Returns")
    plt.xlabel("Return")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Volatility Analysis
    plt.figure(figsize=(12, 6))
    plt.plot(btc_data['volatility_7'], label="7-Day Volatility", alpha=0.7, color='red')
    plt.title("BTC 7-Day Rolling Volatility")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.show()

    # 5. Correlations (Optional)
    print("Correlation Matrix:")
    print(btc_data.corr())

if __name__ == "__main__":
    # Define the input file
    input_csv = "btc_processed_data.csv"
    
    # Perform EDA
    perform_eda(input_csv)
