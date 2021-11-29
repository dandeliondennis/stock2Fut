import numpy as np
import numba as nb


AVGPRICECOL = 13
S1COL = 5
B1COL = 6
AMOUNTCOL = 11
VOLCOL = 10

@nb.njit
def buyAmountRatio(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    avg_price = df[:, AVGPRICECOL]
    sign = (s1past - avg_price) - (avg_price - b1past)
    sign = np.sign(sign)
    signPos = np.maximum(sign, 0)
    return np.nansum(df[:, AMOUNTCOL]*signPos)/(np.nansum(df[:, AMOUNTCOL]) + 0.01)



@nb.njit
def buyAmountRatio1(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price) / np.where(spread == 0, np.nan, spread) - .5
    weight = ratio / np.nansum(np.abs(ratio))
    return np.nansum(df[:, AMOUNTCOL]*weight)/(np.nanmean(df[:, AMOUNTCOL]) + 0.01)



@nb.njit
def buyVolRatio(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    avg_price = df[:, AVGPRICECOL]
    sign = (s1past - avg_price) - (avg_price - b1past)
    sign = np.sign(sign)
    signPos = np.maximum(sign, 0)
    return np.nansum(df[:, VOLCOL]*signPos)/(np.nansum(df[:, VOLCOL]) + 0.01)


@nb.njit
def buyVolRatio1(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, S1COL])) or np.all(np.isnan(df[:, B1COL])):
        return np.nan
    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    avg_price = df[:, AVGPRICECOL]
    spread = s1past - b1past
    ratio = (s1past - avg_price) / np.where(spread == 0, np.nan, spread) - .5
    weight = ratio / np.nansum(np.abs(ratio))
    return np.nansum(df[:, VOLCOL]*weight)/(np.nanmean(df[:, VOLCOL]) + 0.01)


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


calcbuyAmountRatio = lambda df2d: calc(df2d, buyAmountRatio)
calcbuyAmountRatio1 = lambda df2d: calc(df2d, buyAmountRatio1)
calcbuyVolRatio = lambda df2d: calc(df2d, buyVolRatio)
calcbuyVolRatio1 = lambda df2d: calc(df2d, buyVolRatio1)
