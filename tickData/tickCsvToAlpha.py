import pandas as pd
import numpy as np

SYMBOLS = ['AG', 'AL', 'AU', 'BU', 'C', 'CF', 'CU', 'EB', 'EG', 'FG', 'FU',
           'HC', 'I', 'J', 'JM', 'L', 'M', 'MA', 'NI', 'OI', 'P', 'PF', 'PP',
           'RB', 'RM', 'RU', 'SA', 'SC', 'SP', 'TA', 'V', 'Y', 'ZC', 'ZN']

AMENDDATE = pd.to_datetime('2018-04-01')
AMENDINST = 'FU'


def amendFU(df):
    idx = pd.IndexSlice
    df.loc[idx[:AMENDDATE, :], [AMENDINST]] = np.nan
    return df


def tickFactorRead(PATH):
    alphaDF = pd.read_csv(PATH)
    tmp = alphaDF['Unnamed: 0'].apply(lambda string: string[1:-1].split(','))
    alphaDF['date'] = pd.to_datetime(tmp.apply(lambda alist: alist[0]))
    alphaDF['time_flage'] = tmp.apply(lambda alist: int(alist[1]))
    alphaDF.set_index(['date', 'time_flage'], inplace=True)
    del alphaDF['Unnamed: 0']
    return amendFU(alphaDF.sort_index())[SYMBOLS]

