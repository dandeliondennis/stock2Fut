#
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


def calcVolQuantile(df):
    df_shape = (df.shape[0], df.shape[1] + 1)
    vol = df[:, VOLCOL]
    info_num = 17

    if df.shape[0] <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape, info_num, None, None)

    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)

    quantiles = np.nanpercentile(vol, [10, 15, 20, 25, 30, 35, 40,
                                       45, 50, 55, 60, 65, 70, 75,
                                       80, 85, 90])
    ret = np.expand_dims(ret, axis=1)
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret), axis=1),
                           quantiles)


ret_col = 12
distance_col = 13


def smallVolNoise0(struct, para_id):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[para_id]
    if np.isnan(thresh):
        return np.nan
    flag = df[:, VOLCOL] < thresh
    if np.sum(flag) <= 10:
        return np.nan
    ret = df[:, ret_col][flag]
    fenmu = np.nanstd(df[:, ret_col])
    if np.all(np.isnan(ret)) or fenmu == 0:
        return np.nan
    return - np.nanmean(ret) / fenmu


def smallVolNoise0_0(struct):
    return smallVolNoise0(struct, 0)


def smallVolNoise0_1(struct):
    return smallVolNoise0(struct, 1)


def smallVolNoise0_2(struct):
    return smallVolNoise0(struct, 2)


def smallVolNoise0_3(struct):
    return smallVolNoise0(struct, 3)


def smallVolNoise0_4(struct):
    return smallVolNoise0(struct, 4)


def smallVolNoise0_5(struct):
    return smallVolNoise0(struct, 5)


def smallVolNoise0_6(struct):
    return smallVolNoise0(struct, 6)


def smallVolNoise0_7(struct):
    return smallVolNoise0(struct, 7)


def smallVolNoise0_8(struct):
    return smallVolNoise0(struct, 8)


def smallVolNoise0_9(struct):
    return smallVolNoise0(struct, 9)


def smallVolNoise0_10(struct):
    return smallVolNoise0(struct, 10)


def smallVolNoise0_11(struct):
    return smallVolNoise0(struct, 11)


def smallVolNoise0_12(struct):
    return smallVolNoise0(struct, 12)


def smallVolNoise0_13(struct):
    return smallVolNoise0(struct, 13)


def smallVolNoise0_14(struct):
    return smallVolNoise0(struct, 14)


def smallVolNoise0_15(struct):
    return smallVolNoise0(struct, 15)


def smallVolNoise0_16(struct):
    return smallVolNoise0(struct, 16)


def smallVolNoise1(struct, para_id):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[para_id]
    if np.isnan(thresh):
        return np.nan

    flag = df[:, VOLCOL] < thresh
    if np.sum(flag) <= 10:
        return np.nan
    ret_total = df[:, ret_col]
    ret = ret_total[flag]
    fenmu = np.nanstd(ret_total)
    if np.all(np.isnan(ret)) or fenmu == 0:
        return np.nan
    ret_total_mean = np.nanmean(ret_total)
    ret_mean = np.nanmean(ret)
    if (ret_mean * ret_total_mean) > 0:
        return - np.nanmean(ret) / fenmu
    else:
        return 0


def smallVolNoise1_0(struct):
    return smallVolNoise1(struct, 0)


def smallVolNoise1_1(struct):
    return smallVolNoise1(struct, 1)


def smallVolNoise1_2(struct):
    return smallVolNoise1(struct, 2)


def smallVolNoise1_3(struct):
    return smallVolNoise1(struct, 3)


def smallVolNoise1_4(struct):
    return smallVolNoise1(struct, 4)


def smallVolNoise1_5(struct):
    return smallVolNoise1(struct, 5)


def smallVolNoise1_6(struct):
    return smallVolNoise1(struct, 6)


def smallVolNoise1_7(struct):
    return smallVolNoise1(struct, 7)


def smallVolNoise1_8(struct):
    return smallVolNoise1(struct, 8)


def smallVolNoise1_9(struct):
    return smallVolNoise1(struct, 9)


def smallVolNoise1_10(struct):
    return smallVolNoise1(struct, 10)


def smallVolNoise1_11(struct):
    return smallVolNoise1(struct, 11)


def smallVolNoise1_12(struct):
    return smallVolNoise1(struct, 12)


def smallVolNoise1_13(struct):
    return smallVolNoise1(struct, 13)
