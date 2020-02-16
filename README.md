# autocorrelation-stock-predictor
Uses autocorrelation to predict stock price fluctuations based on previous data. 

## How to Use
You must obtain an API key from Alpha Vantage to make requests. The program will NOT work with the current "demo" API key. The code can also be modified to read already downloaded csv files with stock data. Run main.py and the orange line in the pop-up graph window will be the predicted stock price direction:
```
python main.py
```
This alone should not be relied on as an accurate stock predictor, as stock prices can be volatile and subject to many factors.

## Tests
The tests folder contains stock data that the program has been tested on. The tests.py file compares the predicted price fluctuation to the actual price, and it prints out the mean squared error between predicted and actual prices. The tests have shown that the predictions are most accurate for shorter time intervals. As the time intervals increase in the data, the error increases and the accuracy decreases. 

## Credit
* Code adapted from https://github.com/DhruvilKarani/Time-Series-analysisUses
