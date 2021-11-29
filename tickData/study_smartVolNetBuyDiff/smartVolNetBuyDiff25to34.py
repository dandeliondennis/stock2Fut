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
    netBuyVol = df[:, S1COL] - df[:, B1COL]
    res = np.zeros_like(netBuyVol)
    res[1:] = netBuyVol[1:] - netBuyVol[:-1]
    return np.c_[df, flag1, flag2, flag3, flag4, flag5, netBuyVol, res]


flag1_col = 16
flag2_col = 17
flag3_col = 18
flag4_col = 19
flag5_col = 20
netBuyCol = 21
resCol = 22


@nb.njit
def normalize(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += i
        elif i < 0:
            neg += i
        else:
            pass
    if pos == 0 and neg == 0:
        return np.nan
    else:
        return (pos + neg) / (pos - neg)


def smartVolNetBuyDiff25to29(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.compress(df[:, flagCol], df[:, resCol])
    return normalize(res)


smartVolNetBuyDiff25 = lambda df: smartVolNetBuyDiff25to29(df, flag1_col)
smartVolNetBuyDiff26 = lambda df: smartVolNetBuyDiff25to29(df, flag2_col)
smartVolNetBuyDiff27 = lambda df: smartVolNetBuyDiff25to29(df, flag3_col)
smartVolNetBuyDiff28 = lambda df: smartVolNetBuyDiff25to29(df, flag4_col)
smartVolNetBuyDiff29 = lambda df: smartVolNetBuyDiff25to29(df, flag5_col)


def smartVolNetBuyDiff30to34(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.compress(df[:, flagCol], df[:, resCol])
    if np.all(np.isnan(res)):
        return np.nan
    else:
        return np.nanmean(np.sign(res))


smartVolNetBuyDiff30 = lambda df: smartVolNetBuyDiff30to34(df, flag1_col)
smartVolNetBuyDiff31 = lambda df: smartVolNetBuyDiff30to34(df, flag2_col)
smartVolNetBuyDiff32 = lambda df: smartVolNetBuyDiff30to34(df, flag3_col)
smartVolNetBuyDiff33 = lambda df: smartVolNetBuyDiff30to34(df, flag4_col)
smartVolNetBuyDiff34 = lambda df: smartVolNetBuyDiff30to34(df, flag5_col)
