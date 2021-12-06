import numpy as np
import numba as nb

S1COL = 5
B1COL = 6
VOLCOL = 10
SV1COL = 7
BV1COL = 8
LASTPXCOL = 0


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


class CleanedWellData:
    def __init__(self, df_shape, info_num, df=None, info=None):
        self.df_shape = df_shape
        self.info_num = info_num
        if df is None:
            self.df = np.empty(df_shape)
        else:
            self.df = df
        if info is None:
            self.info = np.full(shape=info_num, fill_value=np.nan)
        else:
            self.info = info


def calcVolDiff(df):
    df_shape = [df.shape[0], df.shape[1] + 2]
    info_num = 2
    if df.size == 0:
        return CleanedWellData(df_shape=df_shape, info_num=info_num)
    s1Diff = diff(df[:, S1COL])
    b1Diff = diff(df[:, B1COL])
    sv1Diff = diff(df[:, SV1COL])
    bv1Diff = diff(df[:, BV1COL])
    deltaSV1 = np.where(s1Diff < 0, df[:, SV1COL],
                        np.where(s1Diff == 0, sv1Diff, 0)
                        )
    deltaBV1 = np.where(b1Diff > 0, df[:, BV1COL],
                        np.where(b1Diff == 0, bv1Diff, 0)
                        )
    factor = deltaSV1 - deltaBV1
    factor_abs = np.abs(factor)
    [thresh, thresh1] = np.nanpercentile(factor_abs, [50, 25])
    return CleanedWellData(df_shape, info_num, np.c_[df, factor, factor_abs], np.array([thresh, thresh1]))


ORDER_IMBALANCE = 12
ORDER_IMBALANCE_ABS = 13
