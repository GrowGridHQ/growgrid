# growgrid
Portfolio

This project implements a stock trading algorithm to detect runs (consecutive price increases or decreases) and trigger corresponding 'BUY' or 'SELL' signals. It has been built and demonstrated for the National Stock Exchange of India (NSE).

## Run Detector Algorithm

The `detect_runs` algorithm in `run_detector.py` accepts a series of stock prices and a configurable `run_length`.
- **BUY signal:** Generated after a negative run of `run_length` consecutive periods.
- **SELL signal:** Generated after a positive run of `run_length` consecutive periods.

## How to Run Locally

You should download (clone) these files to your computer to run the algorithm locally. Follow these detailed steps:

**1. Clone the repository**
Open your terminal (or command prompt) and run:
```bash
git clone https://github.com/your-username/growgrid.git
cd growgrid
```
*(Note: Replace the URL with the actual GitHub URL of this repository)*

**2. Set up a virtual environment (Recommended)**
It is best practice to create a virtual environment to install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

**3. Install dependencies**
Install the required libraries (`yfinance`) using the provided requirements file:
```bash
pip install -r requirements.txt
```

**4. Run the NSE Example**
Run the example script, which fetches real historical data for an NSE ticker (`RELIANCE.NS`) and runs the run detector algorithm:
```bash
python nse_example.py
```

**5. Run the Tests (Optional)**
If you want to verify that the core algorithm is working correctly, you can run the unit tests:
```bash
python -m unittest test_run_detector.py
```
