# 这个文件的目的是为了给因子29进行参数选择

import numpy as np


LASTCOL = 0
VOLCOL = 10


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
    info_num = 6
    if df.shape[0] <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape=df_shape, info_num=info_num)
    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)
    ret = ret.reshape(-1, 1)
    quantiles = np.nanpercentile(vol, [75, 80, 85, 92.5, 95, 90])
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret), axis=1),
                           quantiles)


ret_col = 12


# 对应75分位数
def smartVol28_0(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[0]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan

    fenmu = np.nanstd(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应80分位数
def smartVol28_1(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[1]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应85分位数
def smartVol28_2(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[2]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应92.5分位数
def smartVol28_3(struct):
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


# 对应95分位数
def smartVol28_4(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[4]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应75分位数
def smartVol27_0(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[0]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan

    fenmu = np.nanstd(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应80分位数
def smartVol27_1(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[1]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应85分位数
def smartVol27_2(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[2]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


# 对应92.5分位数
def smartVol27_3(struct):
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


# 对应95分位数
def smartVol27_4(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[4]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


def smartVol27_test(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[5]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


def smartVol28_test(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[5]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanstd(ret_sub)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu


def smartVol29_test(struct):
    df = struct.df
    if df.size == 0:
        return np.nan
    thresh = struct.info[5]
    ret_all = df[:, ret_col]
    ret_sub = ret_all[df[:, VOLCOL] > thresh]
    if np.all(np.isnan(ret_sub)):
        return np.nan
    fenmu = np.nanmax(ret_all) - np.nanmin(ret_all)
    if fenmu == 0:
        return np.nan
    return np.nanmean(ret_sub) / fenmu
