import numpy as np
import numba as nb


AVGPRICECOL = 13
S1COL = 5
B1COL = 6
AMOUNTCOL = 11
VOLCOL = 10

@nb.njit
def avgLocation(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = df[:, S1COL]
    b1past = df[:, B1COL]
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price)/np.where(spread==0, np.nan, spread) - .5
    return np.nanmean(ratio)


@nb.njit
def avgLocation1(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = df[:, S1COL]
    b1past = df[:, B1COL]
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price)/np.where(spread==0, np.nan, spread) - .5
    ratio = np.where(np.abs(ratio) > 0.25, ratio, 0)
    return np.nanmean(ratio)


@nb.njit
def avgLocation2(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = df[:, S1COL]
    b1past = df[:, B1COL]
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price)/np.where(spread==0, np.nan, spread) - .5
    ratio = np.sign(ratio)
    return np.nanmean(ratio)


@nb.njit
def avgLocation3(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = df[:, S1COL]
    b1past = df[:, B1COL]
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price)/np.where(spread==0, np.nan, spread) - .5
    ratioStd = np.nanstd(ratio)
    ratio = np.where(np.abs(ratio) > 0.25*ratioStd, ratio, 0)
    return np.nanmean(ratio)



def splitData(datalist):
    if len(datalist) >= 1:
        return datalist[-1]
    else:
        return None


def calc(datalist, func):
    tmp = splitData(datalist)
    if tmp.size>0:
        return func(tmp)
    else:
        return np.nan


calcAvgLocation = lambda df2d: calc(df2d, avgLocation)
calcAvgLocation1 = lambda df2d: calc(df2d, avgLocation1)
calcAvgLocation2 = lambda df2d: calc(df2d, avgLocation2)
calcAvgLocation3 = lambda df2d: calc(df2d, avgLocation3)
