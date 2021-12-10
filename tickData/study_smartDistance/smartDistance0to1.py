#
import numba as nb
import numpy as np
from numba import float64, int32, types
from numba.experimental import jitclass

LASTCOL = 0
VOLCOL = 10

shape_type = types.UniTuple(types.int32, count=2)
spec1 = [('df_shape', shape_type),
        ('info_num', int32),
        ('df', float64[:, :]),
        ('info', float64[:])]


@jitclass(spec=spec1)
class CleanedWellData:
    def __init__(self, df_shape, info_num, df, info):
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


jitCleanedWellData = nb.extending.as_numba_type(CleanedWellData)


@nb.njit(float64[:](float64[:]))
def diff(arr):
    res = np.zeros(arr.shape)
    res[1:] = arr[1:] - arr[:-1]
    return res


@nb.njit(jitCleanedWellData(float64[:, :]))
def calcDistance(df):
    df_shape = (df.shape[0], df.shape[1] + 2)
    vol = df[:, VOLCOL]
    info_num = 4
    if df.shape[0] <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape, info_num, None, None)
    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)
    ret_uniform = ret / np.nanmax(np.abs(ret)) / 2
    vol_uniform = vol / np.nanmax(vol)
    distance = np.square(ret_uniform) + np.square(vol_uniform)
    quantiles = np.nanpercentile(distance, [80, 85, 90, 95])

    ret = np.expand_dims(ret, axis=1)
    distance = np.expand_dims(distance, axis=1)
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret, distance), axis=1),
                           quantiles)


ret_col = 12
distance_col = 13


@nb.njit(float64(jitCleanedWellData, int32))
def smartDistance0(struct, para_id):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[para_id]
    ret = df[:, ret_col][df[:, distance_col] > thresh]
    print(len(ret))
    fenmu = np.nanstd(df[:, ret_col])
    if np.all(np.isnan(ret)) or fenmu == 0:
        return np.nan
    return np.nanmean(ret) / fenmu


# 因子0_0对应80分位数的sharpe
def smartDistance0_0(struct):
    return smartDistance0(struct, 0)


# 因子0_1对应85分位数的sharpe
def smartDistance0_1(struct):
    return smartDistance0(struct, 1)


# 因子0_2对应90分位数的sharpe
def smartDistance0_2(struct):
    return smartDistance0(struct, 2)


# 因子0_3对应95分位数的sharpe
def smartDistance0_3(struct):
    return smartDistance0(struct, 3)


def smartDistance1(struct, para_id):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[para_id]
    flag = (df[:, distance_col] > thresh)
    vol = df[:, VOLCOL]
    ret_weighted = df[:, ret_col] * vol / np.nansum(vol)
    ret_weighted = ret_weighted[flag]
    fenmu = np.nanstd(df[:, ret_col])
    if np.all(np.isnan(ret_weighted)) or fenmu == 0:
        return np.nan
    return np.nanmean(ret_weighted) / fenmu


# 因子1_0对应80分位数的sharpe
def smartDistance1_0(struct):
    return smartDistance1(struct, 0)


# 因子1_1对应85分位数的sharpe
def smartDistance1_1(struct):
    return smartDistance0(struct, 1)


# 因子1_2对应90分位数的sharpe
def smartDistance1_2(struct):
    return smartDistance0(struct, 2)


# 因子1_3对应95分位数的sharpe
def smartDistance1_3(struct):
    return smartDistance0(struct, 3)
