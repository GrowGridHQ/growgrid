import yfinance as yf
from run_detector import detect_runs

def main():
    ticker = "RELIANCE.NS"
    print(f"Fetching historical data for {ticker} from Yahoo Finance...")

    # Fetch 1 year of daily historical data
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")

    if hist.empty:
        print(f"Failed to fetch data for {ticker}.")
        return

    # Extract closing prices
    closing_prices = hist['Close'].tolist()
    dates = hist.index.strftime('%Y-%m-%d').tolist()

    run_length = 3
    print(f"\nDetecting runs (run_length={run_length})...")

    # Run our algorithm
    signals = detect_runs(closing_prices, run_length)

    print("\nRecent Signals detected:")
    print("-" * 50)

    # Count total signals
    buy_count = 0
    sell_count = 0
    total_signals = signals.count('BUY') + signals.count('SELL')

    for i in range(len(signals)):
        signal = signals[i]
        if signal:
            if signal == 'BUY':
                buy_count += 1
            elif signal == 'SELL':
                sell_count += 1

            # Only print the most recent 10 signals for brevity
            if (buy_count + sell_count) > (total_signals - 10):
                 print(f"Date: {dates[i]} | Price: {closing_prices[i]:.2f} | Signal: {signal}")

    print("-" * 50)
    print(f"Total over the past year:")
    print(f"BUY signals: {buy_count}")
    print(f"SELL signals: {sell_count}")


if __name__ == "__main__":
    main()
