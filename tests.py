import requests
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA

scaler = MinMaxScaler(feature_range=(0, 1))

df = pd.read_csv("tests/intraday_15min_BA.csv")

df_stocks = df.iloc[:len(df) - 100, 3]
df_holdout = df.iloc[len(df) - 100:, 3]

df_stocks_diff = df_stocks - df_stocks.shift()
df_stocks_diff.iloc[0] = df_stocks.iloc[0]

lag_acf = acf(df_stocks, nlags=10)
lag_pacf = pacf(df_stocks, nlags=10, method="ols")

model = ARIMA(df_stocks, order=(2,1,1))
results_AR = model.fit(disp=-1)

predictions_AR = results_AR.predict(start=len(df_stocks_diff), end=len(df_stocks_diff) + (len(df) - len(df_stocks_diff) - 1))
predictions_AR.iloc[0] = predictions_AR.iloc[0] + df_stocks.iloc[len(df_stocks_diff) - 1]
predictions_AR = predictions_AR.cumsum()
predictions_AR.index = df_holdout.index

plt.plot(df_stocks)
plt.plot(df_holdout)
plt.plot(predictions_AR)

error = mean_squared_error(df_holdout, predictions_AR)
print("Error: ", str(error))

plt.show()