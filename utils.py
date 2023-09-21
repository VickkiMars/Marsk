import details
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import date
from dateutil.relativedelta import relativedelta
import datetime as dt
from alpaca.trading.client import TradingClient
from sklearn.preprocessing import MinMaxScaler

past_days = 50
client = TradingClient(details.KEY_ID, details.SECRET_KEY, paper=True)

trading_pair = 'ETH/USD'
today = date.today()
past = dt.timedelta(days=past_days)
tast = today-past

class MarskUtils():
    def __init__(self, trading_pair):
        def getAllData():
            data_client = CryptoHistoricalDataClient()
            from datetime import datetime
            time_diff = datetime.now() - relativedelta(hours=1000)
            print("Getting bar data for {0} starting from {1}".format(trading_pair, time_diff))
            request_params = CryptoBarsRequest(symbol_or_symbols=[trading_pair], timeframe = TimeFrame.Hour, start=time_diff)
            df = data_client.get_crypto_bars(request_params).df
            global current_price
            current_price = df.iloc[-1]['close']
            return df

        def getFeature(feature, df):
            data = df.filter([feature])
            data = data.values
            return data

        def scaleData(data):
            scaler = MinMaxScaler(Feature_range=(-1,1))
            scaled_data = scaler.fit_transform(data)
            return scaled_data, scaler


        def getTrainData(scaled_data):
            x, y = [], []
            for price in range(100, len(scaled_data)):
                x.append(scaled_data[price-100:price])

        getFeature('close', getAllData())
