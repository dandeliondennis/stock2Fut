import numpy as np
import numba as nb
from numba import float64, int32


@nb.njit(float64[:](float64[:], int32))
def cumGap(arr, nums):
    # arr must be a non-negative array
    total = np.nansum(arr)
    gapThresh = 1 / nums * total
    tmpSum = 0
    gapArr = np.zeros_like(arr)

    for idx, i in enumerate(arr):
        if np.isnan(i):
            continue
        tmpSum += i
        if tmpSum > gapThresh:
            gapArr[idx] = 1
            tmpSum = 0
        else:
            pass
    return gapArr


@nb.njit
def normalize(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += i
        elif i < 0:
            neg += i
        else:
            pass
    if pos == 0 and neg == 0:
        return np.nan
    else:
        return (pos + neg) / (pos - neg)


LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14

GAPNUM = 1000


def downSampleByVol(df):
    nrow, ncol = df.shape
    if nrow <= 3600:
        return np.empty([1, ncol])
    gapArr, gapSet = cumGap(df[:, VOLCOL], GAPNUM)
    return np.compress(gapArr, df, axis=0)


def simpleRSI(df):
    if df.shape[0] <= 1:
        return np.nan
    price = df[:, LASTPXCOL]
    priceDiff = np.zeros_like(price)
    priceDiff[1:] = price[1:] - price[:-1]
    return normalize(priceDiff)


def simpleSignSum(df):
    if df.shape[0] <= 1:
        return np.nan
    price = df[:, LASTPXCOL]
    priceDiff = np.zeros_like(price)
    priceDiff[1:] = np.sign(price[1:] - price[:-1])
    if np.all(np.isnan(priceDiff)):
        return np.nan
    return np.nanmean(priceDiff)


def simpleSharpe0(df):
    if df.shape[0] <= 1:
        return np.nan
    price = df[:, LASTPXCOL]
    ret = np.zeros_like(price)
    ret[1:] = np.log(price[1:] / price[:-1])

    tmp = np.nanstd(ret)
    if tmp == 0:
        return np.nan
    return np.nanmean(ret) / tmp


def simpleSharpe1(df):
    if df.shape[0] <= 1:
        return np.nan
    price = df[:, LASTPXCOL]
    priceDiff = np.zeros_like(price)
    priceDiff[1:] = price[1:] - price[:-1]
    pathLength = np.nansum(np.abs(priceDiff))
    if pathLength == 0:
        return np.nan
    return (price[-1] - price[0]) / pathLength


volDownSample0 = simpleRSI
volDownSample1 = simpleSignSum
volDownSample2 = simpleSharpe0
volDownSample3 = simpleSharpe1
