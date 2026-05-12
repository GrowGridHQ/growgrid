# growgrid
Portfolio

This project implements a stock trading algorithm to detect runs (consecutive price increases or decreases) and trigger corresponding 'BUY' or 'SELL' signals. It has been built and demonstrated for the National Stock Exchange of India (NSE).

## Run Detector Algorithm

The `detect_runs` algorithm in `run_detector.py` accepts a series of stock prices and a configurable `run_length`.
- **BUY signal:** Generated after a negative run of `run_length` consecutive periods.
- **SELL signal:** Generated after a positive run of `run_length` consecutive periods.

## NSE Example
To see the algorithm in action on real Indian market data, install `yfinance`:

```bash
pip install yfinance
```

Then run the NSE example script, which fetches historical data for `RELIANCE.NS` and runs the detector:

```bash
python nse_example.py
```
