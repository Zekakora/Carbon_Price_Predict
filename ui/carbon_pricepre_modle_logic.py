import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from keras.callbacks import Callback

def get_data(path, type):
    if type == 'EXCEL':
        df = pd.read_excel(path)
    elif type == 'CSV':
        df = pd.read_csv(path)
    else:
        return 0

    df.dropna(inplace=True)
    # data = df.set_index('time', drop=True)
    # print(df.head(5))
    return df, df.head(3), df.columns


def iso_tree(df):
    iso = IsolationForest(random_state=1, contamination='auto')
    preds = iso.fit_predict(df.values)
    df['cluster'] = preds
    print(df['cluster'].value_counts().sort_values(ascending=False))
    df = df[df['cluster'] != -1].drop(columns=['cluster'])
    print("处理后的数据框形状：", df.shape)
    return df


# df = get_data('D:/OneDrive/Projects/Coding/Dachuang_20232024/data/bjtotal.xlsx','EXCEL')

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from pandas import DataFrame
from pandas import concat
from keras import regularizers
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, Bidirectional, BatchNormalization, Dropout
from keras.layers import LSTM

from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras import regularizers
from keras.callbacks import EarlyStopping


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # 输入序列(t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # 预测序列(t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # 把所有放在一起
    agg = concat(cols, axis=1)
    agg.columns = names
    # 删除空值行
    if dropnan:
        agg.dropna(inplace=True)
    return agg


def prepare_data(df, n_in, ratio):
    values = df.values
    values = values.astype('float32')
    reframed = series_to_supervised(values, n_in, 1)
    reframed.drop(reframed.columns[-7:-1], axis=1, inplace=True)
    print(reframed.head(3))

    scaler_s = StandardScaler()
    scaler_0 = MinMaxScaler(feature_range=(0, 1))

    values = reframed.values
    values = scaler_s.fit_transform(values)

    n_train_hours = int(len(values) * float(ratio))
    train = values[:n_train_hours, :]
    test = values[n_train_hours:, :]

    # train = scaler_s.fit_transform(train)
    # test = scaler_s.transform(test)
    train_x, train_y = train[:, :-1], train[:, -1]
    test_x, test_y = test[:, :-1], test[:, -1]

    train_x = train_x.reshape(train_x.shape[0], 1, train_x.shape[1])
    test_x = test_x.reshape(test_x.shape[0], 1, test_x.shape[1])

    print(train_x.shape, train_y.shape)
    return train_x, train_y, test_x, test_y

class LSTMmodel:
    def __init__(self, input_shape, units=50):
        self.input_shape = input_shape
        self.units = units
        self.model = self.build_model(input_shape)
        self.history = None

    def build_model(self, input_shape, units=100):
        model = Sequential()
        model.add(LSTM(256, input_shape=input_shape, return_sequences=True))
        model.add(Dropout(0.1))
        model.add(LSTM(128, return_sequences=True))  # 添加一个额外的LSTM层
        model.add(Dropout(0.1))  # 添加Dropout层
        model.add(LSTM(1280))  # 将第二个LSTM层改为32个单元
        model.add(Dense(units=32, activation='relu', kernel_regularizer=regularizers.l2(0.01)))  # 减少Dense层中的单元数量
        model.add(Dropout(0.2))  # 保留Dropout层
        model.add(Dense(units=1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        return model

    def train(self, train_x, train_y, epochs=50, batch_size=32, validation_data=None):
        # callbacks = [EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)]
        self.history = self.model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, validation_data=validation_data)

    def predict(self, X):
        return self.model.predict(X)

    def showmodel(self):
        print(self.model.summary())

    def save(self, path, rename):
        print(path+'/'+rename+'.h5')
        self.model.save(path+'/'+rename+'.keras',save_format='tf')

    def get_loss_history(self):
        loss = self.history.history['loss']
        val_loss = self.history.history['val_loss']
        print(self.history.history)
        return loss, val_loss

def cookdata(df, ratio):
    train_x, train_y, test_x, test_y = prepare_data(df, 90, ratio)
    return train_x, train_y, test_x, test_y

def train_model(df, ratio, batch_size, epochs, mpath, rename):
    train_x, train_y, test_x, test_y = prepare_data(df, 90, ratio)
    LSTM_model = LSTMmodel(input_shape=train_x.shape[1:], units=100)
    LSTM_model.train(train_x, train_y, epochs=epochs, batch_size=batch_size, validation_data=(test_x, test_y))
    loss, val_loss = LSTM_model.get_loss_history()
    LSTM_model.showmodel()
    LSTM_model.save(mpath,rename)
    return train_x, train_y, test_x, test_y, loss, val_loss

from keras.models import load_model

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
def test_model(mpath, data_x, data_y):
    LoadModel = load_model(mpath)
    print('123')
    outresult = LoadModel.predict(data_x)

    mse = mean_squared_error(outresult, data_y)
    r2 = r2_score(outresult, data_y)
    mae = mean_absolute_error(outresult, data_y)

    return outresult, mse, r2, mae
