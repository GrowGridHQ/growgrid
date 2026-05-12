def detect_runs(prices, run_length):
    """
    Detects runs in a series of prices and returns a list of signals ('BUY', 'SELL', or None).
    A 'BUY' signal is generated after a negative run of `run_length`.
    A 'SELL' signal is generated after a positive run of `run_length`.

    This function can be applied to any stock market data, including NSE tickers
    (e.g., RELIANCE.NS, INFY.NS).

    Args:
        prices (list of float/int): The historical prices.
        run_length (int): The number of consecutive periods of increase/decrease to trigger a signal.

    Returns:
        list of str/None: Signals corresponding to each price point.
    """
    if run_length <= 0:
        raise ValueError("run_length must be a positive integer")

    signals = []
    current_run = 0

    for i in range(len(prices)):
        if i == 0:
            signals.append(None)
            continue

        if prices[i] > prices[i-1]:
            if current_run < 0:
                current_run = 1
            else:
                current_run += 1
        elif prices[i] < prices[i-1]:
            if current_run > 0:
                current_run = -1
            else:
                current_run -= 1
        else:
            current_run = 0

        if current_run >= run_length:
            signals.append('SELL')
        elif current_run <= -run_length:
            signals.append('BUY')
        else:
            signals.append(None)

    return signals
