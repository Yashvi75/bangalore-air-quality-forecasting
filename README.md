Bangalore Air Quality Forecasting

Overview:
This project performs time series analysis and forecasting of PM2.5 air pollution levels in Bengaluru using statistical methods. The objective is to analyze temporal patterns and build a predictive model using ARIMA.

Dataset:
Source: Kaggle – Air Quality Data in India
Filtered for: Bengaluru
Key Feature: PM2.5 concentration (daily data)

Methodology:
Data preprocessing and cleaning
Time series visualization and moving average
Seasonal decomposition
Stationarity testing (ADF Test)
ARIMA modeling and parameter tuning (AIC-based)
Forecasting and evaluation

Model:
Model Used: ARIMA
Train-Test Split: 80:20
Evaluation Metric: Mean Absolute Error (MAE)

Results:
MAE: 12.13
Model captures general trend but struggles with sharp fluctuations due to high data volatility

Tech Stack:
Python
Pandas, NumPy
Matplotlib
Statsmodels
Scikit-learn

Project Structure:
bangalore-air-quality-forecasting/
│
├── data/
├── notebooks/
├── src/
├── reports/
├── requirements.txt
└── README.md


Conclusion:
ARIMA provides a solid baseline for time series forecasting but has limitations in modeling highly volatile environmental data. Future improvements can include advanced models like LSTM.