import numpy as np

PRICECOL = 3
S1COL = 6
B1COL = 7


def calcRet(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    price = df[:, PRICECOL]
    ret = np.zeros_like(price)
    ret[1:] = np.log(price[1:] / price[:-1])
    volNaN = np.isnan(df[:, VOLCOL])
    price1 = df[:, S1COL]
    ret1 = np.zeros_like(price1)
    ret1[1:] = np.log(price1[1:] / price1[:-1])
    price2 = df[:, B1COL]
    ret2 = np.zeros_like(price2)
    ret2[1:] = np.log(price2[1:] / price2[:-1])
    ret3 = np.zeros_like(price2)
    ret3[1:] = np.log((price1[1:] + price2[1:]) / (price1[:-1] + price2[:-1]))
    return np.c_[df, ret, volNaN, ret1, ret2, ret3]


RETCOL = 15
VOLNANCOL = 16
RET1COL = 17
RET2COL = 18
RET3COL = 19
VOLCOL = 11


def tickMom12(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 0.75
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RETCOL])) / (np.sum(realVol) + 0.01)


def tickMom13(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 1
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RETCOL])) / (np.sum(realVol) + 0.01)


def tickMom14(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 0.75
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RET1COL])) / (np.sum(realVol) + 0.01)


def tickMom15(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 1
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RET1COL])) / (np.sum(realVol) + 0.01)


def tickMom16(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 0.75
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RET2COL])) / (np.sum(realVol) + 0.01)


def tickMom17(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 1
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RET2COL])) / (np.sum(realVol) + 0.01)


def tickMom18(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 0.75
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RET3COL])) / (np.sum(realVol) + 0.01)


def tickMom19(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL]) * 1
    realVol = np.where(df[:, VOLCOL] > volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * np.sign(df[:, RET3COL])) / (np.sum(realVol) + 0.01)
