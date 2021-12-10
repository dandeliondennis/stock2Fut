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
    nrow, ncol = df.shape
    add_col = 5
    df_shape = (nrow, ncol + add_col)
    vol = df[:, VOLCOL]
    info_num = 4

    if nrow <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape, info_num, None, None)

    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)
    ret_max = np.nanmax(np.abs(ret))
    vol_max = np.nanmax(vol)
    if (ret_max == 0) or (vol_max == 0):
        return CleanedWellData(df_shape, info_num, None, None)

    ret_para = np.array([0.5, 1, 64, 10000000])
    distance_thresh = np.full_like(ret_para, np.nan, dtype=np.float64)
    distance_total = np.full((nrow, ncol + 4), np.nan, dtype=np.float64, order='F')
    vol_uniform_square = np.square(vol / vol_max)
    ret1 = ret / ret_max
    for idx, para in enumerate(ret_para):
        ret_uniform = ret1 / para
        distance = np.square(ret_uniform) + vol_uniform_square
        quantiles = np.nanpercentile(distance, 90)
        distance_thresh[idx] = quantiles
        distance_total[:, idx] = distance
    ret = np.expand_dims(ret, axis=1)
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret, distance_total), axis=1),
                           distance_thresh)


ret_col = 12
distance_col = {0: 13, 1: 14, 2: 15, 3: 16}


def smartDistance2(struct, para_id):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[para_id]
    flag = df[:, distance_col[para_id]] > thresh
    if np.sum(flag) <= 10:
        return np.nan
    ret = df[:, ret_col][flag]
    fenmu = np.nanstd(df[:, ret_col])
    if np.all(np.isnan(ret)) or fenmu == 0:
        return np.nan
    return np.nanmean(ret) / fenmu


# 因子2_0对应ret_square/4
def smartDistance2_4(struct):
    return smartDistance2(struct, 0)


# 因子2_1对应对应ret_square/8
def smartDistance2_5(struct):
    return smartDistance2(struct, 1)


# 因子2_2对应对应ret_square/16
def smartDistance2_6(struct):
    return smartDistance2(struct, 2)


# 因子2_3对应对应ret_square/32
def smartDistance2_7(struct):
    return smartDistance2(struct, 3)
