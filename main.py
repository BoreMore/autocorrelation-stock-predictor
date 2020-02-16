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

apikey = "demo"
symbol = "BA"
interval = 15 # acceptable: 1, 5, 15, 30, 60
csvfile = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=" + str(interval) + "min&apikey=" + apikey + "&datatype=csv&outputsize=full")

filename = "intraday" + "_" + str(interval) + "min" + "_" + symbol + ".csv"

with open(filename, "wb") as f:
    f.write(csvfile.content)

df = pd.read_csv(filename)

df_stocks = df.iloc[:, 3]

df_stocks_diff = df_stocks - df_stocks.shift()
df_stocks_diff.iloc[0] = df_stocks.iloc[0]

lag_acf = acf(df_stocks, nlags=10)
lag_pacf = pacf(df_stocks, nlags=10, method="ols")

model = ARIMA(df_stocks, order=(2,1,1))
results_AR = model.fit(disp=-1)

predict_range = 100
predictions_AR = results_AR.predict(start=len(df_stocks_diff), end=len(df_stocks_diff) + predict_range)
predictions_AR.iloc[0] = predictions_AR.iloc[0] + df_stocks.iloc[len(df_stocks_diff) - 1]
predictions_AR = predictions_AR.cumsum()
predictions_AR.index = np.arange(len(df_stocks_diff), len(df_stocks_diff) + predict_range + 1)

plt.plot(df_stocks)
plt.plot(predictions_AR)

plt.show()