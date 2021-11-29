import numpy as np

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14


def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    tmp = df[:, S1COL] * df[:, SV1COL] - df[:, B1COL] * df[:, BV1COL]
    netBuyDiff = np.zeros_like(tmp)
    netBuyDiff[1:] = tmp[1:] - tmp[:-1]
    return np.c_[df, tmp, netBuyDiff]


TMPCOL = 16
DIFFCOL = 17


def sellBuyAmountDiff40_43(df, threshNum):
    if len(df) <= 3600:
        return np.nan
    netBuyDiff = df[:, DIFFCOL]
    if np.all(np.isnan(netBuyDiff)):
        return np.nan
    netBuyDiffStd = np.nanstd(netBuyDiff)
    thresh = threshNum * netBuyDiffStd
    res = np.where(np.abs(netBuyDiff) < thresh, np.sign(netBuyDiff), 0)
    return np.nanmean(res)


sellBuyAmountDiff40 = lambda df: sellBuyAmountDiff40_43(df, 0.25)
sellBuyAmountDiff41 = lambda df: sellBuyAmountDiff40_43(df, 0.5)
sellBuyAmountDiff42 = lambda df: sellBuyAmountDiff40_43(df, 0.75)
sellBuyAmountDiff43 = lambda df: sellBuyAmountDiff40_43(df, 0.1)


def sellBuyAmountDiff44_47(df, threshNum):
    if len(df) <= 3600:
        return np.nan
    netBuyDiff = df[:, DIFFCOL]
    if np.all(np.isnan(netBuyDiff)):
        return np.nan
    netBuyDiffStd = np.nanstd(netBuyDiff)
    thresh = threshNum * netBuyDiffStd
    res = np.where(np.abs(netBuyDiff) < thresh, 0, -np.sign(netBuyDiff))
    return np.nanmean(res)

sellBuyAmountDiff44 = lambda df: sellBuyAmountDiff44_47(df, 0.25)
sellBuyAmountDiff45 = lambda df: sellBuyAmountDiff44_47(df, 0.5)
sellBuyAmountDiff46 = lambda df: sellBuyAmountDiff44_47(df, 0.75)
sellBuyAmountDiff47 = lambda df: sellBuyAmountDiff44_47(df, 0.1)