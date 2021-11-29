import numpy as np
import numba as nb

S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3


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


def diff(arr):
    res = np.zeros_like(arr)
    res[1:] = arr[1:] - arr[:-1]
    return res


def calcVolDiff(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 6])
    s1Diff = diff(df[:, S1COL])
    b1Diff = diff(df[:, B1COL])
    sv1Diff = diff(df[:, SV1COL])
    bv1Diff = diff(df[:, BV1COL])
    vol = df[:, VOLCOL]
    deltaSV1 = np.where(s1Diff == -1, df[:, SV1COL] + vol,
                        np.where(s1Diff == 0, sv1Diff + vol, 0)
                        )
    deltaBV1 = np.where(b1Diff == 1, df[:, BV1COL] + vol,
                        np.where(b1Diff == 0, bv1Diff + vol, 0)
                        )
    return np.c_[df, s1Diff, b1Diff, sv1Diff, bv1Diff, deltaSV1, deltaBV1]


S1DIFF = 16
B1DIFF = 17
SV1DIFF = 18
BV1DIFF = 19
SV1DELTA = 20
BV1DELTA = 21


def orderImbalance_1(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, SV1DELTA] - df[:, BV1DELTA])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def orderImbalance_2(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, SV1DELTA] - df[:, BV1DELTA]
    return normalize(tmp)
