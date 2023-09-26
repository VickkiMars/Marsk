"""
Module containing strategies that could be used in the trading bot
"""
import pandas as pd
class MarskStrategy:
    def __init__(self, data, short_win, long_win):
        self.data = pd.read_csv(data)
        self.short_win = short_win
        self.long_win = long_win

    def tfs(self, data, short_win, long_win):
        '''
        tfs: Trend Following Strategy
        - Identify and follow the prevailing market trend using EMA's (Exponential Moving Average) or SMA's (Simple Moving Average) or both.
        - When the short term moving average crosses above the long term moving average, we buy.
        - When the short term moving average crosses below the long-term moving average, we sell.
        '''
        data['SMA_short'] = data['Close'].rolling(window=short_win).mean() #
        data['SMA_long'] = data['Close'].rolling(window=long_win).mean()

        data["trend"] = np.where(data["Close"] > data["SMA_short"], 1, -1) #

        for i in range(len(data)):
            if data.loc[i, "trend"] == 1:
                print("Buy at", data.loc[i, "Close"])
            elif data.loc[i, "trend"] == -1:
                print("Sell at", data.loc[i, "Close"])

    def backtest_tfs(self):

        #Calculate Moving Average
        data["SMA_short"] = data["Close"].rolling(window=20).mean()
        data["SMA_long"] = data["Close"].rolling(window=50).mean()

        #Define the strategy
        data["signal"] = 0
        data.loc[data["SMA_short"] > data["SMA_long"], "signal"] = 1
        data.loc[data["SMA_short"] < data["SMA_long"], "signal"] = -1

        # Backtesting
        data["position"] = data["signal"].shift()
        data["returns"] = data["position"] * data[price].pct_change()

        # Calculate cumulative returns
        data["cum_returns"] = (1 + data["returns"]).cumprod()

        #Plot cumulative returns
        data["cum_returns"].plot()
