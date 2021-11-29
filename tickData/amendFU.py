import pandas as pd

AMENDDATE = pd.to_datetime('2018-04-01')
AMENDINST = 'FU'


def amendFU(df):
    idx = pd.IndexSlice
    df.loc[idx[:AMENDDATE, :], [AMENDINST]] = 0
    return df
