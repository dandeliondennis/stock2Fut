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
    return np.c_[df, tmp]


TMPCOL = 16


def sellBuyAmountDiff36(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMPCOL]
    netBuyDiff = np.zeros_like(tmp)
    netBuyDiff[1:] = tmp[1:] - tmp[:-1]
    if np.all(np.isnan(netBuyDiff)):
        return np.nan
    netBuyDiffStd = np.nanstd(netBuyDiff)
    thresh = 0.25 * netBuyDiffStd
    res = np.where(np.abs(netBuyDiff) < thresh, np.sign(netBuyDiff), -np.sign(netBuyDiff))
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


def sellBuyAmountDiff37(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMPCOL]
    netBuyDiff = np.zeros_like(tmp)
    netBuyDiff[1:] = tmp[1:] - tmp[:-1]
    if np.all(np.isnan(netBuyDiff)):
        return np.nan
    netBuyDiffStd = np.nanstd(netBuyDiff)
    thresh = 0.5 * netBuyDiffStd
    res = np.where(np.abs(netBuyDiff) < thresh, np.sign(netBuyDiff), -np.sign(netBuyDiff))
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


def sellBuyAmountDiff38(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMPCOL]
    netBuyDiff = np.zeros_like(tmp)
    netBuyDiff[1:] = tmp[1:] - tmp[:-1]
    if np.all(np.isnan(netBuyDiff)):
        return np.nan
    netBuyDiffStd = np.nanstd(netBuyDiff)
    thresh = 0.75 * netBuyDiffStd
    res = np.where(np.abs(netBuyDiff) < thresh, np.sign(netBuyDiff), -np.sign(netBuyDiff))
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


def sellBuyAmountDiff39(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMPCOL]
    netBuyDiff = np.zeros_like(tmp)
    netBuyDiff[1:] = tmp[1:] - tmp[:-1]
    if np.all(np.isnan(netBuyDiff)):
        return np.nan
    netBuyDiffStd = np.nanstd(netBuyDiff)
    thresh = netBuyDiffStd
    res = np.where(np.abs(netBuyDiff) < thresh, np.sign(netBuyDiff), -np.sign(netBuyDiff))
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)
