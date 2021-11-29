import numpy as np
import numba as nb

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14


def calcVolOrder(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 7])
    vol = df[:, VOLCOL]
    if np.all(np.isnan(vol)):
        tmp = np.zeros_like(vol)
        return np.c_[df, tmp, tmp, tmp, tmp, tmp, tmp, tmp]
    lowVol, quarter, median_, three_quarter, highVol = np.nanpercentile(vol, [10, 25, 50, 75, 90])
    flag1 = np.where(vol < lowVol, 0, 1)
    flag2 = np.where(vol < quarter, 0, 1)
    flag3 = np.where(vol < median_, 0, 1)
    flag4 = np.where(vol < three_quarter, 0, 1)
    flag5 = np.where(vol < highVol, 0, 1)
    netBuy = df[:, SV1COL] * df[:, S1COL] - df[:, BV1COL] * df[:, B1COL]
    res = np.zeros_like(netBuy)
    res[1:] = netBuy[1:] - netBuy[:-1]
    return np.c_[df, flag1, flag2, flag3, flag4, flag5, res, netBuy]


flag1_col = 16
flag2_col = 17
flag3_col = 18
flag4_col = 19
flag5_col = 20
netBuyDiffCol = 21
netBuyCol = 22


def smartVolNetBuyDiff0to4(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.sign(np.compress(df[:, flagCol], df[:, netBuyDiffCol]))
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


smartVolNetBuyDiff0 = lambda df: smartVolNetBuyDiff0to4(df, flag1_col)
smartVolNetBuyDiff1 = lambda df: smartVolNetBuyDiff0to4(df, flag2_col)
smartVolNetBuyDiff2 = lambda df: smartVolNetBuyDiff0to4(df, flag3_col)
smartVolNetBuyDiff3 = lambda df: smartVolNetBuyDiff0to4(df, flag4_col)
smartVolNetBuyDiff4 = lambda df: smartVolNetBuyDiff0to4(df, flag5_col)


def smartVolNetBuyDiff5to9(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.compress(df[:, flagCol], df[:, netBuyCol])
    resDiff = np.zeros_like(res)
    resDiff[1:] = np.sign(res[1:] - res[:-1])
    if np.all(np.isnan(resDiff)):
        return np.nan
    return np.nanmean(resDiff)


smartVolNetBuyDiff5 = lambda df: smartVolNetBuyDiff5to9(df, flag1_col)
smartVolNetBuyDiff6 = lambda df: smartVolNetBuyDiff5to9(df, flag2_col)
smartVolNetBuyDiff7 = lambda df: smartVolNetBuyDiff5to9(df, flag3_col)
smartVolNetBuyDiff8 = lambda df: smartVolNetBuyDiff5to9(df, flag4_col)
smartVolNetBuyDiff9 = lambda df: smartVolNetBuyDiff5to9(df, flag5_col)
