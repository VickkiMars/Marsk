import math
import datetime as dt
import numpy as np
import pandas as pd
from tensorflow import keras
from datetime import datetime, date
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

class stockPred:
    def __init__(self,
    key1: str,
    key2: str,
    past_days: int = 50,
    trading_pair: str = 'BTCUSD',
    exchange: str = 'FTXU',
    feature: str = 'close',

    look_back: int = 72,
    split_perc: int = .8,

    neurons: int = 50,
    activ_func: str = 'linear',
    dropout: float = 0.2,
    loss: str = 'mse',
    optimizer: str = 'adam',
    epochs: int = 20,
    batch_size: int = 32,
    output_size: int = 1,

    plot: bool = True,

    mse_thresh: float = .002,
    r2_thresh: float = .8
    ):
        self.key1 = key1
        self.key2 = key2
        self.history = datetime.timedelta(days = past_days)
        self.trading_pair = trading_pair
        self.exchange = exchange
        self.feature = feature

        self.look_back = look_back
        self.split_perc = split_perc

        #LSTM Model
        self.neurons = neurons
        self.activ_func = activ_func
        self.dropout = dropout
        self.loss = loss
        self.optimizer = optimizer
        self.epochs = epochs
        self.batch_size = batch_size
        self.output_size = output_size

        self.plot = plot

        # thresholds for model training
        self.mse_thresh = mse_thresh
        self.r2_thresh = r2_thresh

    def getAllData(self):
        data
