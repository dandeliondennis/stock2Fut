import numpy as np
import numba as nb

AVGPRICECOL = 13
S1COL = 5
B1COL = 6
AMOUNTCOL = 11
VOLCOL = 10


@nb.njit
def buyVolRatioPiecewise(df, para):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price) / np.where(spread == 0, np.nan, spread) - .5
    ratioStd = np.nanstd(ratio)
    weight = np.where(ratio > para * ratioStd, 1,
                      np.where(ratio < -para * ratioStd, 0, 0.5))
    return np.nansum(df[:, VOLCOL] * weight) / (np.nansum(df[:, VOLCOL]) + 0.01)


def splitData(datalist):
    if len(datalist) >= 1:
        return datalist[-1]
    else:
        return None


def calc(datalist, para):
    tmp = splitData(datalist)
    if tmp.size > 0:
        return buyVolRatioPiecewise(tmp, para)
    else:
        return np.nan


calcbuyVolRatioPiecewiseStd1 = lambda df2d: calc(df2d, 0.1)
calcbuyVolRatioPiecewiseStd2 = lambda df2d: calc(df2d, 0.2)
calcbuyVolRatioPiecewiseStd3 = lambda df2d: calc(df2d, 0.3)
calcbuyVolRatioPiecewiseStd4 = lambda df2d: calc(df2d, 0.4)
