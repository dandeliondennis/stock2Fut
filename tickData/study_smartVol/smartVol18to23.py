import numpy as np
import numba as nb

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14


def calcVolOrder(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 4])
    vol = df[:, VOLCOL]
    if np.all(np.isnan(vol)):
        tmp = np.zeros_like(vol)
        return np.c_[df, tmp, tmp, tmp, tmp]
    median, quarter, low = np.nanpercentile(vol, [50, 25, 10])
    flag1 = np.where(vol > quarter, 1, 0)
    flag2 = np.where(vol > low, 1, 0)
    flag3 = np.where(vol > median, 1, 0)
    ret = np.zeros_like(df[:, LASTPXCOL])
    ret[1:] = np.log(df[:, LASTPXCOL][1:] / df[:, LASTPXCOL][:-1])
    return np.c_[df, flag1, flag2, flag3, ret]


flag1_col = 16
flag2_col = 17
flag3_col = 17
ret_col = 19


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
def smartVol18(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret * df[:, flag1_col])


@nb.njit
def smartVol19(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret * df[:, flag2_col])


@nb.njit
def smartVol20(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret * df[:, flag3_col])


@nb.njit
def smartVol21(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return np.nansum(ret * df[:, flag1_col])


@nb.njit
def smartVol22(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return np.nansum(ret * df[:, flag2_col])


@nb.njit
def smartVol23(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return np.nansum(ret * df[:, flag3_col])
