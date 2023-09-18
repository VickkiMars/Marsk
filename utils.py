import math
import numpy as np
import pandas as pd
from tensorflow import keras
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
