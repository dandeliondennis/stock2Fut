import numpy as np
import numba as nb

S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3
thresh, thresh1 = 0, 0


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
def diff(arr):
    res = np.zeros_like(arr)
    res[1:] = arr[1:] - arr[:-1]
    return res


@nb.njit
def nanFunc(arr, func):
    if np.all(np.isnan(arr)):
        return np.nan
    notNaNIdx = ~np.isnan(arr)
    res = func(arr[notNaNIdx])
    return res


def calcVolDiff(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    s1Diff = diff(df[:, S1COL])
    b1Diff = diff(df[:, B1COL])
    sv1Diff = diff(df[:, SV1COL])
    bv1Diff = diff(df[:, BV1COL])
    deltaSV1 = np.where(s1Diff == -1, df[:, SV1COL],
                        np.where(s1Diff == 0, sv1Diff, 0)
                        )
    deltaBV1 = np.where(b1Diff == 1, df[:, BV1COL],
                        np.where(b1Diff == 0, bv1Diff, 0)
                        )
    factor = deltaSV1 - deltaBV1
    factor_abs = np.abs(factor)
    global thresh, thresh1
    [thresh, thresh1] = np.nanpercentile(factor_abs, [50, 25])
    return np.c_[df, factor, factor_abs]


ORDER_IMBALANCE = 16
ORDER_IMBALANCE_ABS = 17


def orderImbalance_3(df):
    if df.size == 0:
        return np.nan
    factor = df[:, ORDER_IMBALANCE]
    factor_abs = df[:, ORDER_IMBALANCE_ABS]
    factorBound = np.where(factor_abs > thresh, np.sign(factor) * thresh, factor)
    print(thresh, np.nanpercentile(factor_abs, 50))
    return normalize(factorBound)


def orderImbalance_4(df):
    if df.size == 0:
        return np.nan
    factor = df[:, ORDER_IMBALANCE]

    factor_abs = df[:, ORDER_IMBALANCE_ABS]
    factorBound = np.where(factor_abs > thresh, 0, factor)
    return normalize(factorBound)


def orderImbalance_5(df):
    if df.size == 0:
        return np.nan
    factor = df[:, ORDER_IMBALANCE]
    factor_abs = df[:, ORDER_IMBALANCE_ABS]
    factorBound = np.where(factor_abs > thresh1, np.sign(factor) * thresh, factor)
    return normalize(factorBound)


def orderImbalance_6(df):
    if df.size == 0:
        return np.nan
    factor = df[:, ORDER_IMBALANCE]
    factor_abs = df[:, ORDER_IMBALANCE_ABS]
    factorBound = np.where(factor_abs > thresh1, 0, factor)
    return normalize(factorBound)
