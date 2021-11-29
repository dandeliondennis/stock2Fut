import numpy as np

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14


def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 1])
    tmp = df[:, S1COL] * df[:, SV1COL] - df[:, B1COL] * df[:, BV1COL]
    return np.c_[df, tmp]


TMPCOL = 16


def arrRollingApply(arr, window, func):
    nlen = arr.size
    res = np.full(nlen, np.nan)
    for i in range(window, nlen + 1):
        res[i - 1] = func(arr[i - window:i])
    return res


def sellBuyAmountDiff0(df):
    if df.size == 0:
        return np.nan

    tmp = np.sign(df[:, SV1COL] - df[:, BV1COL])
    return np.nansum(tmp)


def sellBuyAmountDiff1(df):
    if df.size == 0:
        return np.nan

    tmp = np.sign(df[:, TMPCOL])
    return np.nansum(tmp)


def sellBuyAmountDiff2(df):
    if df.size == 0:
        return np.nan

    tmp = df[:, TMPCOL]
    tmp = np.sign(arrRollingApply(tmp, 5, np.sum))
    return np.nansum(tmp)


def sellBuyAmountDiff3(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, TMPCOL])
    tmp = arrRollingApply(tmp, 5, np.sum)
    return np.nansum(tmp)


def sellBuyAmountDiff4(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    tmp = np.sign(arrRollingApply(tmp, 10, np.sum))
    return np.nansum(tmp)


def sellBuyAmountDiff5(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, TMPCOL])
    tmp = arrRollingApply(tmp, 10, np.sum)
    return np.nansum(tmp)


def sellBuyAmountDiff6(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    res = np.zeros(tmp.shape)
    res[1:] = np.sign(tmp[1:] - tmp[:-1])
    return np.nansum(res)
