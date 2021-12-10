#
import line_profiler
import numpy as np
import warnings

warnings.filterwarnings("error")

LASTCOL = 0
VOLCOL = 10


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


def calcDistance(df):
    df_shape = (df.shape[0], df.shape[1] + 2)
    vol = df[:, VOLCOL]
    info_num = 4

    if df.shape[0] <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape, info_num, None, None)

    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)
    ret_max = np.nanmax(np.abs(ret))
    vol_max = np.nanmax(vol)
    if (ret_max == 0) or (vol_max == 0):
        return CleanedWellData(df_shape, info_num, None, None)

    ret_uniform = ret / ret_max / 2
    vol_uniform = vol / vol_max
    distance = np.square(ret_uniform) + np.square(vol_uniform)
    quantiles = np.nanpercentile(distance, [80, 85, 90, 95])
    ret = np.expand_dims(ret, axis=1)
    distance = np.expand_dims(distance, axis=1)
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret, distance), axis=1),
                           quantiles)


ret_col = 12
distance_col = 13


def smartDistance0(struct, para_id):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[para_id]
    flag = df[:, distance_col] > thresh
    if np.sum(flag) <= 10:
        return np.nan
    ret = df[:, ret_col][flag]
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
    if np.sum(flag) <= 10:
        return np.nan
    vol = df[:, VOLCOL]
    vol_ = vol[flag]
    vol_sum = np.nansum(vol_)
    if vol_sum == 0:
        return np.nan
    ret_weighted = df[:, ret_col][flag]
    ret_weighted = ret_weighted * vol_ / vol_sum
    fenmu = np.nanstd(df[:, ret_col])
    if np.all(np.isnan(ret_weighted)) or fenmu == 0:
        return np.nan
    return np.nansum(ret_weighted) / fenmu


# 因子1_0对应80分位数的sharpe
def smartDistance1_0(struct):
    return smartDistance1(struct, 0)


# 因子1_1对应85分位数的sharpe
def smartDistance1_1(struct):
    return smartDistance1(struct, 1)


# 因子1_2对应90分位数的sharpe
def smartDistance1_2(struct):
    return smartDistance1(struct, 2)


# 因子1_3对应95分位数的sharpe
def smartDistance1_3(struct):
    return smartDistance1(struct, 3)
