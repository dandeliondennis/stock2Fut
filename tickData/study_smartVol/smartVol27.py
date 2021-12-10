# 这个文件的目的是为了给因子27 进行不同周期的选择

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
    info_num = 1
    if df.shape[0] <= 1200 or np.all(np.isnan(vol)):
        return CleanedWellData(df_shape=df_shape, info_num=info_num)
    ret = np.diff(np.log(df[:, LASTCOL]), prepend=np.nan)
    ret = ret.reshape(-1, 1)
    quantiles = np.nanpercentile(vol, [90])
    return CleanedWellData(df_shape, info_num,
                           np.concatenate((df, ret), axis=1),
                           quantiles)


ret_col = 12


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
