import numpy as np
import pandas as pd
import os

PATH = 'C:/tick/{}_{}'
fileList = os.listdir('C:/tick')
tdatelist = [i[:-2] for i in fileList[::3]]
SYMBOLS = ['AG', 'AL', 'AU', 'BU', 'C', 'CF', 'CU', 'EB', 'EG', 'FG', 'FU',
           'HC', 'I', 'J', 'JM', 'L', 'M', 'MA', 'NI', 'OI', 'P', 'PF', 'PP',
           'RB', 'RM', 'RU', 'SA', 'SC', 'SP', 'TA', 'V', 'Y', 'ZC', 'ZN']
timeFlage = [1, 2, 3]


def readTickData(path):
    tmp = pd.read_csv(path,
                      usecols=['LastPrice', 'HighestPrice', 'LowestPrice',
                               'Volume', 'Turnover', 'AskPrice1', 'BidPrice1', 'AskVolume1', 'BidVolume1',
                               'OpenInterest'],
                      dtype={
                          'LastPrice': np.float64,
                          'HighestPrice': np.float64,
                          'LowestPrice': np.float64,
                          'Volume': np.float64,
                          'Turnover': np.float64,
                          'AskPrice1': np.float64,
                          'BidPrice1': np.float64,
                          'AskVolume1': np.float64,
                          'BidVolume1': np.float64,
                          'OpenInterest': np.float64},
                      engine='c')

    return tmp


Volume = 3
Turnover = 4
AskPrice1 = 5
BidPrice1 = 6


def handleTickData(arr2d):
    arr2d[:, [AskPrice1, BidPrice1]] = np.where(arr2d[:, [AskPrice1, BidPrice1]] == 0, np.nan,
                                                arr2d[:, [AskPrice1, BidPrice1]])
    vol = np.diff(arr2d[:, Volume], prepend=np.nan)
    vol = np.where(vol < 0.1, np.nan, vol)
    amount = np.diff(arr2d[:, Turnover], prepend=np.nan)
    amount = np.where(amount < 0.1, np.nan, amount)
    vol = vol.reshape((-1,1))
    amount = amount.reshape((-1,1))
    return np.concatenate((arr2d, vol, amount), axis=1)


def handleTickDataComplete(df):
    if df.empty:
        return np.empty([df.shape[0], df.shape[1] + 2])
    else:
        return handleTickData(np.array(df, order='F'))


def readFunc(para):
    tdate, timeflage = para
    data = {}
    directory = PATH.format(tdate, timeflage)

    for root, dirs, files in os.walk(directory):
        for file in files:
            name, fileType = file.split('.')
            if fileType == "csv":
                filePath = ''.join([directory, '/', file])
                data[name] = handleTickDataComplete(readTickData(filePath))
    return data
