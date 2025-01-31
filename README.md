# Stock-Analysis

A stock market analysis and prediction web application built using Streamlit - Python. The project utilizes machine learning models (Linear Regression, Random Forest, LSTM) to predict stock prices and visualize stock trends.

## Features

- Fetches real-time stock data using `yfinance`.
- Supports multiple prediction models: Linear Regression, Random Forest, and LSTM.
- Displays stock charts using `plotly`.
- Identifies top gainers and losers in Sensex and Nifty.
- Deployable on Streamlit and Flask.

## Installation

### Prerequisites

- Python 3.10+
- Virtual environment (`venv` or `conda` recommended)
- Required dependencies (listed in `requirements.txt`)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/Yuvan-1166/Stock-Analysis.git
   cd stock-predictor
   ```
2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Streamlit application:
   ```sh
   streamlit run Home.py
   ```

## Usage

- Enter the stock ticker, start date, and end date.
- Choose a prediction model to forecast future stock prices.
- View stock trends, gainers, and losers in interactive charts.

## Models Used

- **Linear Regression**: Simple and interpretable model for stock trend analysis.
- **Random Forest**: Provides better generalization and robustness.
- **LSTM (Long Short-Term Memory)**: Captures sequential patterns in stock data.

## Exporting & Using Trained Models

- Trained models are saved as `.pkl` files using `joblib`.
- Example:
  ```python
  import joblib
  scaler = joblib.load('scaler.pkl')
  model = joblib.load('stock_predictor_model.pkl')
  ```

## Contributing

- Fork the repo and create a new branch.
- Implement changes and submit a pull request.
- Ensure proper documentation and testing.

## Author

Developed by [Yuvan Shankar S](https://github.com/Yuvan-1166).

## Contact

For queries or collaboration, email: yuvanshankars.1166@google.com
