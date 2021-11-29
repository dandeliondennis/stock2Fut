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


def volAdjustedMom5(df):
    if df.size == 0:
        return np.nan
    volReturn = np.where(df[:, TRCOL] > 0,
                         (df[:, PRICECOL] - df[:, LASTPRICE]) / (df[:, TRCOL] + 0.01),
                         0)
    return np.sum(volReturn)


def volAdjustedMom6(df):
    if df.size == 0:
        return np.nan
    high, low = np.nanpercentile(df[:, PRICECOL], [95, 5])
    if high > low:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / (high - low)
    else:
        return np.nan


def volAdjustedMom7(df):
    if df.size == 0:
        return np.nan
    high, low = np.nanpercentile(df[:, PRICECOL], [85, 15])
    if high > low:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / (high - low)
    else:
        return np.nan


def volAdjustedMom8(df):
    if df.size == 0:
        return np.nan
    high, low = np.nanpercentile(df[:, PRICECOL], [80, 20])
    if high > low:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / (high - low)
    else:
        return np.nan


def volAdjustedMom9(df):
    if df.size == 0:
        return np.nan
    high, low = np.nanpercentile(df[:, PRICECOL], [75, 25])
    if high > low:
        return (df[:, PRICECOL][-1] - df[:, PRICECOL][0]) / (high - low)
    else:
        return np.nan


def volAdjustedMom10(df):
    if df.size == 0:
        return np.nan
    first, third = np.nanpercentile(df[:, RETCOL], [25, 75])
    if third>first:
        return (third  + first)/(third - first)
    return np.nan