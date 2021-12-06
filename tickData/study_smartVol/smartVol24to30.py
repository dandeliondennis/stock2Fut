import numpy as np
import numba as nb
from numba import float64

LASTCOL = 0
VOLCOL = 10


@nb.njit(float64(float64[:]))
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


def calcVolQuantile(df):
    df_shape = (df.shape[0], df.shape[1] + 1)
    vol = df[:, VOLCOL]
    info_num = 5
    if df.shape[0] <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape=df_shape, info_num=info_num)
    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)
    ret = ret.reshape(-1, 1)
    quantiles = np.nanpercentile(vol, [75, 80, 85, 90, 92.5])
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret), axis=1),
                           quantiles)


ret_col = 12


# 因子24对应80分位数的normalize
def smartVol24(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[1]
    ret = df[:, ret_col][df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret)


# 因子25对应85分位数的normalize
def smartVol25(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[2]
    ret = df[:, ret_col][df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret)


# 因子26对应92.5分位数的normalize
def smartVol26(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[4]
    ret = df[:, ret_col][df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret)):
        return np.nan
    return normalize(ret)


# 因子27对应90分位数的， 经过波动率调整后的因子
# 目前使用的波动率调整的方法是 除以整个的波动率
def smartVol27(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[3]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 因子28对应90分位数的， 经过波动率调整后的因子
# 目前使用的波动率调整的方法是 除以筛选后收益率的波动率
def smartVol28(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[3]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 因子29对应90分位数的， 经过波动率调整后的因子
# 目前使用的波动率调整的方法是 除以全部的range
def smartVol29(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[3]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanmax(ret_all) - np.nanmin(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 因子30对应90分位数的， 经过波动率调整后的因子
# 目前使用的波动率调整的方法是 除以筛选后的range
def smartVol30(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[3]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanmax(ret_sub) - np.nanmin(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu
