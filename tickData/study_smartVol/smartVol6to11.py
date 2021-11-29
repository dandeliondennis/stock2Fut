import numpy as np
import numba as nb

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14


def calcRetOrder(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    ret = np.zeros_like(df[:, LASTPXCOL])
    ret[1:] = np.log(df[:, LASTPXCOL][1:]/df[:, LASTPXCOL][:-1])
    low, quarter, three_quarter, high = np.nanpercentile(ret, [10, 25, 75, 90])
    flag1 = np.where(ret < low, -1,
                     np.where(ret > high, 1, 0)
                     )
    flag2 = np.where(ret < quarter, -1,
                     np.where(ret > three_quarter, 1, 0)
                     )
    return np.c_[df, flag1, flag2]


flag1_col = 16
flag2_col = 17

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
    if (pos - neg) == 0:
        return np.nan
    else:
        return (pos + neg) / (pos - neg)


@nb.njit
def smartVol6(df):
    if len(df) <= 3600:
        return np.nan
    vol = df[:, VOLCOL]
    if np.all(np.isnan(vol)):
        return np.nan
    return normalize(vol * df[:, flag1_col])


@nb.njit
def smartVol7(df):
    if len(df) <= 3600:
        return np.nan
    vol = df[:, VOLCOL]
    if np.all(np.isnan(vol)):
        return np.nan
    return normalize(vol * df[:, flag2_col])


def smartVol8(df):
    if len(df) <= 3600:
        return np.nan
    nlen = len(df)
    weights = np.linspace(-1, 1, num=nlen)
    weights = weights/np.sum(np.abs(weights))
    if np.all(np.isnan(df[:, flag1_col])):
        return np.nan
    return np.nansum(weights * df[:, flag1_col])


def smartVol9(df):
    if len(df) <= 3600:
        return np.nan
    nlen = len(df)
    weights = np.linspace(-1, 1, num=nlen)
    weights = weights / np.sum(np.abs(weights))
    if np.all(np.isnan(df[:, flag2_col])):
        return np.nan
    return np.nansum(weights * df[:, flag2_col])


def smartVol10(df):
    if len(df) <= 3600:
        return np.nan
    if np.all(np.isnan(df[:, VOLCOL])):
        return np.nan
    if np.all(np.isnan(df[:, flag2_col])):
        return np.nan
    nlen = len(df)
    weights1 = np.linspace(-1, 1, num=nlen)
    weights2 = df[:, VOLCOL]/np.nansum(df[:, VOLCOL])
    weight = weights1*weights2
    weight = weight/np.nansum(np.abs(weight))
    if np.all(np.isnan(df[:, flag1_col])):
        return np.nan
    return np.nansum(weight * df[:, flag1_col])


def smartVol11(df):
    if len(df) <= 3600:
        return np.nan
    if np.all(np.isnan(df[:, VOLCOL])):
        return np.nan
    if np.all(np.isnan(df[:, flag2_col])):
        return np.nan
    nlen = len(df)
    weights1 = np.linspace(-1, 1, num=nlen)
    weights2 = df[:, VOLCOL]/np.nansum(df[:, VOLCOL])
    weight = weights1*weights2
    weight = weight/np.nansum(np.abs(weight))
    return np.nansum(weight * df[:, flag2_col])