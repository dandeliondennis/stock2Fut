import numpy as np

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
OICOL = 12
VOLCOL = 13
AMOUNTCOL = 14


def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    tmp1 = df[:, S1COL] * df[:, SV1COL] - df[:, B1COL] * df[:, BV1COL]
    tmp2 = df[:, S1COL] / df[:, B1COL] * df[:, SV1COL] - df[:, BV1COL]
    return np.c_[df, tmp1, tmp2]


TMP1COL = 16
TMP2COL = 17


def sellBuyAmountDiff7(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = np.sign(tmp[1:] - tmp[:-1])
    return np.nanmean(res)


def sellBuyAmountDiff8(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP2COL]
    res = np.zeros(tmp.shape)
    res[1:] = np.sign(tmp[1:] - tmp[:-1])
    return np.nanmean(res)


def sellBuyAmountDiff9(df):
    if len(df) <= 3600:
        return np.nan
    oi = df[:, OICOL]
    oi[oi == 0] = np.nan
    if np.all(np.isnan(oi)):
        return np.nan
    tmp = df[:, TMP1COL] / oi * 1000
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    return np.nanmean(res)


def sellBuyAmountDiff10(df):
    if len(df) <= 3600:
        return np.nan
    oi = df[:, OICOL]
    oi[oi == 0] = np.nan
    if np.all(np.isnan(oi)):
        return np.nan
    tmp = df[:, TMP2COL] / oi * 1000
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    return np.nanmean(res)


def sellBuyAmountDiff11(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[res < (0.25 * resStd)] = 0
    return np.nanmean(res)


def sellBuyAmountDiff12(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP2COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[res < (0.25 * resStd)] = 0
    return np.nanmean(res) * 100
