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
        return np.c_[df, tmp, tmp, tmp]
    three_quarter, high, extreme = np.nanpercentile(vol, [75, 90, 95])
    flag1 = np.where(vol > high, 1, 0)
    flag2 = np.where(vol > three_quarter, 1, 0)
    flag3 = np.where(vol > extreme, 1, 0)
    ret = np.zeros_like(df[:, LASTPXCOL])
    ret[1:] = np.log(df[:, LASTPXCOL][1:]/df[:, LASTPXCOL][:-1])
    return np.c_[df, flag1, flag2, flag3, ret]


flag1_col = 16
flag2_col = 17
flag3_col = 18
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
def smartVol12(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret * df[:, flag1_col])


@nb.njit
def smartVol13(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret * df[:, flag2_col])


@nb.njit
def smartVol14(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret * df[:, flag3_col])



@nb.njit
def smartVol15(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return np.nansum(ret * df[:, flag1_col])


@nb.njit
def smartVol16(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return np.nansum(ret * df[:, flag2_col])


@nb.njit
def smartVol17(df):
    if len(df) <= 3600:
        return np.nan
    ret = df[:, ret_col]
    if np.all(np.isnan(ret)):
        return np.nan
    return np.nansum(ret * df[:, flag3_col])