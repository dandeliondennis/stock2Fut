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
    data = {}
    for inst in SYMBOLS:
        tmpDF = pd.read_csv(PATH.format(inst))
        tmp = tmpDF['Unnamed: 0'].apply(lambda string: string.split('_'))
        tmpDF['date'] = pd.to_datetime(tmp.apply(lambda alist: alist[0]))
        tmpDF['time_flage'] = tmp.apply(lambda alist: int(alist[1]))
        tmpDF.set_index(['date', 'time_flage'], inplace=True)
        del tmpDF['Unnamed: 0']
        data[inst] = tmpDF

    alpha = pd.concat(data.values(), axis=1)
    '''
    tmp1 = alpha.index
    tmp2 = alpha.sort_index().index
    print(tmp1.is_lexsorted(), tmp2.is_lexsorted())
    print(len(tmp1), len(tmp2))
    print(np.all(tmp1==tmp2))
    '''
    return amendFU(alpha.sort_index())

