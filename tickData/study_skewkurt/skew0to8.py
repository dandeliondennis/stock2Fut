import numpy as np

PRICECOL = 3


def calcRet(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 1])
    price = df[:, PRICECOL]
    ret = np.zeros_like(price)
    ret[1:] = np.log(price[1:] / price[:-1])
    return np.c_[df, ret]


RETCOL = 16


def skew0(df):
    if df.size == 0:
        return np.nan
    fenmu = np.nanmean(df[:, RETCOL] ** 2)
    if fenmu > 0:
        return np.nanmean(df[:, RETCOL] ** 3) / (fenmu ** 1.5)
    else:
        return np.nan


def skew1(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, RETCOL])
    ret = df[:, RETCOL] - avg
    fenmu = np.nanmean(ret ** 2)
    if fenmu > 0:
        return np.nanmean(ret ** 3) / (fenmu ** 1.5)
    else:
        return np.nan


def skew2(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, RETCOL])
    median = np.nanmedian(df[:, RETCOL])
    return avg - median


def skew3(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, RETCOL])
    tmp = np.sign(df[:, RETCOL] - avg)
    return np.nanmean(tmp)


def skew4(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, RETCOL])
    diff = df[:, RETCOL] - avg
    diffAbs = np.abs(diff)
    thresh = np.nanmean(diffAbs)
    diff[diffAbs < thresh] = 0
    return np.nanmean(np.sign(diff))


def skew5(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, PRICECOL])
    ret = df[:, PRICECOL] - avg
    fenmu = np.nanmean(ret ** 2)
    if fenmu > 0:
        return np.nanmean(ret ** 3) / (fenmu ** 1.5)
    else:
        return np.nan


def skew6(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, PRICECOL])
    median = np.nanmedian(df[:, PRICECOL])
    return avg / median - 1


def skew7(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, PRICECOL])
    tmp = np.sign(df[:, PRICECOL] - avg)
    return np.nanmean(tmp)


def skew8(df):
    if df.size == 0:
        return np.nan
    avg = np.nanmean(df[:, PRICECOL])
    diff = df[:, PRICECOL] - avg
    diffAbs = np.abs(diff)
    thresh = np.nanmean(diffAbs)
    diff[diffAbs < thresh] = 0
    return np.nanmean(np.sign(diff))
