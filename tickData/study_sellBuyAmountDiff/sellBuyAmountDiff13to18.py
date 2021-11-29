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
        return np.empty([df.shape[0], df.shape[1] + 1])
    tmp1 = df[:, S1COL] * df[:, SV1COL] - df[:, B1COL] * df[:, BV1COL]
    return np.c_[df, tmp1]


TMP1COL = 16
TMP2COL = 17


def sellBuyAmountDiff13(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[np.abs(res) < (0.25 * resStd)] = 0
    return np.nansum(np.sign(res))


def sellBuyAmountDiff14(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[np.abs(res) < (0.5 * resStd)] = 0
    return np.nansum(np.sign(res))


def sellBuyAmountDiff15(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[np.abs(res) < (0.75 * resStd)] = 0
    return np.nansum(np.sign(res))


def sellBuyAmountDiff16(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[np.abs(res) < (0.25 * resStd)] = 0
    return np.nanmean(np.sign(res))


def sellBuyAmountDiff17(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[np.abs(res) < (0.5 * resStd)] = 0
    return np.nanmean(np.sign(res))


def sellBuyAmountDiff18(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMP1COL]
    res = np.zeros(tmp.shape)
    res[1:] = tmp[1:] - tmp[:-1]
    resStd = np.nanstd(res)
    res[np.abs(res) < (0.75 * resStd)] = 0
    return np.nanmean(np.sign(res))





