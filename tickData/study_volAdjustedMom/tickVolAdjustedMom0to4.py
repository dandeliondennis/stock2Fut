import numpy as np

PRICECOL = 3
HIGHCOL = 4
LOWCOL = 5


def calcRet(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    price = df[:, PRICECOL]
    ret = np.zeros_like(price)
    ret[1:] = np.log(price[1:] / price[:-1])
    lastPrice = np.roll(df[:, PRICECOL], 1)
    lastPrice[0] = np.nan
    tr = np.maximum(df[:, HIGHCOL], lastPrice) - np.minimum(df[:, LOWCOL], lastPrice)
    return np.c_[df, ret, tr, lastPrice]


RETCOL = 15
TRCOL = 16
LASTPRICE = 17


def volAdjustedMom0(df):
    if df.size == 0:
        return np.nan
    high = np.nanmax(df[:, PRICECOL])
    low = np.nanmin(df[:, PRICECOL])
    if high > low:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / (high - low)
    else:
        return np.nan


def volAdjustedMom1(df):
    if df.size == 0:
        return np.nan
    high, low = np.nanpercentile(df[:, PRICECOL], [90, 10])
    if high > low:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / (high - low)
    else:
        return np.nan


def volAdjustedMom2(df):
    if df.size == 0:
        return np.nan
    nrow, ncol = df.shape
    res = 0
    splitSize = 3
    for i in range(splitSize):
        start = (nrow // splitSize) * i
        if i == splitSize - 1:
            end = nrow
        else:
            end = (nrow // splitSize) * (i + 1)
        split = df[:, PRICECOL][start:end]
        if len(split) == 0:
            res += 0
            continue
        else:
            pass
        high, low = np.nanmax(split), np.nanmin(split)
        first, last = split[0], split[-1]
        if high > low:
            res += (last - first) / (high - low)
        else:
            res += 0
        return res


def volAdjustedMom3(df):
    if df.size == 0:
        return np.nan
    trSum = np.nansum(df[:, TRCOL])
    if trSum > 0:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / trSum
    else:
        return np.nan


def volAdjustedMom4(df):
    if df.size == 0:
        return np.nan
    nrow, ncol = df.shape
    res = 0
    splitSize = 3
    for i in range(splitSize):
        start = (nrow // splitSize) * i
        if i == splitSize - 1:
            end = nrow
        else:
            end = (nrow // splitSize) * (i + 1)
        split = df[:, PRICECOL][start:end]
        if len(split) == 0:
            res += 0
            continue
        else:
            pass
        trSum = np.nansum(df[:, TRCOL][start:end])
        first, last = split[0], split[-1]
        if trSum > 0:
            res += (last - first) / trSum
        else:
            res += 0
        return res



