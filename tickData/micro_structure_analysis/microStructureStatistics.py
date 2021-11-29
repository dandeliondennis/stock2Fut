import numpy as np

PRICECOL = 3
S1COL = 4
B1COL = 5
SV1COL = 6
BV1COL = 7
VOLCOL = 8
OICOL = 12


def calcRet(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 1])
    price = df[:, PRICECOL]
    ret = np.zeros_like(price)
    ret[1:] = np.log(price[1:] / price[:-1])
    return np.c_[df, ret]


RETCOL = 16


def s1Ratio(df):
    if df.size == 0:
        return np.nan
    s1ratio = np.where(df[:, VOLCOL] > 0, df[:, SV1COL] / (df[:, VOLCOL] + 0.01), np.nan)
    if np.all(np.isnan(s1ratio)):
        return np.nan
    else:
        return np.nanmean(s1ratio)


def b1Ratio(df):
    if df.size == 0:
        return np.nan
    b1ratio = np.where(df[:, VOLCOL] > 0, df[:, BV1COL] / (df[:, VOLCOL] + 0.01), np.nan)
    if np.all(np.isnan(b1ratio)):
        return np.nan
    else:
        return np.nanmean(b1ratio)


def s1Ratio1(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, SV1COL])) or np.all(np.isnan(df[:, VOLCOL])):
        return np.nan
    s1total = np.nansum(df[:, SV1COL])
    voltotal = np.nansum(df[:, VOLCOL])
    if voltotal > 0:
        return s1total / voltotal
    return np.nan


def b1Ratio1(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, BV1COL])) or np.all(np.isnan(df[:, VOLCOL])):
        return np.nan
    b1total = np.nansum(df[:, BV1COL])
    voltotal = np.nansum(df[:, VOLCOL])
    if voltotal > 0:
        return b1total / voltotal
    return np.nan


def skew(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, RETCOL])):
        return np.nan
    avg = np.nanmean(df[:, RETCOL])
    tmp = df[:, RETCOL] - avg
    if np.nansum(np.abs(tmp)) == 0:
        return np.nan
    return np.nanmean(tmp ** 3) / (np.nanmean(tmp ** 2) ** 1.5)


def kurtosis(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, RETCOL])):
        return np.nan
    avg = np.nanmean(df[:, RETCOL])
    tmp = df[:, RETCOL] - avg
    if np.nansum(np.abs(tmp)) == 0:
        return np.nan
    return np.nanmean(tmp ** 4) / (np.nanmean(tmp ** 2) ** 2)


def tjd(df):
    if df.size == 0:
        return np.nan
    if df[:, OICOL][-1] > 0:
        return np.nansum(df[:, VOLCOL]) / df[:, OICOL][-1]
    else:
        return np.nan


def spread(df):
    if df.size == 0:
        return np.nan
    spread = df[:, S1COL] - df[:, B1COL]
    if np.all(np.isnan(spread)):
        return np.nan
    return np.nanmean(spread)
