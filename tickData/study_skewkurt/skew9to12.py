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


def quantile_skew(quantile):
    if quantile[2] - quantile[0] != 0:
        return ((quantile[2] - quantile[1]) - (quantile[1] - quantile[0]))/(quantile[2] - quantile[0])
    else:
        return np.nan


def skew9(df):
    if df.size == 0:
        return np.nan
    ret_quantile = np.nanpercentile(df[:, RETCOL], [25, 50, 75])

    return quantile_skew(ret_quantile)


def skew10(df):
    if df.size == 0:
        return np.nan
    price_quantile = np.nanpercentile(df[:, PRICECOL], [25, 50, 75])
    return quantile_skew(price_quantile)


def skew11(df):
    if df.size == 0:
        return np.nan
    ret_quantile = np.nanpercentile(df[:, RETCOL], [15, 50, 85])
    return quantile_skew(ret_quantile)


def skew12(df):
    if df.size == 0:
        return np.nan
    price_quantile = np.nanpercentile(df[:, PRICECOL], [15, 50, 85])
    return quantile_skew(price_quantile)



