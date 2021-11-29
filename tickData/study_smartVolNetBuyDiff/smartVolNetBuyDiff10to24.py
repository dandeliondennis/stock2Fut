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
        return np.empty([df.shape[0], df.shape[1] + 6])
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
    res = np.zeros_like(df[:, LASTPXCOL])
    res[1:] = df[:, LASTPXCOL][1:] - df[:, LASTPXCOL][:-1]
    return np.c_[df, flag1, flag2, flag3, flag4, flag5, res]


flag1_col = 16
flag2_col = 17
flag3_col = 18
flag4_col = 19
flag5_col = 20
resCol = 21


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


def smartVolNetBuyDiff10to14(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.compress(df[:, flagCol], df[:, resCol])
    if np.all(np.isnan(res)):
        return np.nan
    return normalize(res)


smartVolNetBuyDiff10 = lambda df: smartVolNetBuyDiff10to14(df, flag1_col)
smartVolNetBuyDiff11 = lambda df: smartVolNetBuyDiff10to14(df, flag2_col)
smartVolNetBuyDiff12 = lambda df: smartVolNetBuyDiff10to14(df, flag3_col)
smartVolNetBuyDiff13 = lambda df: smartVolNetBuyDiff10to14(df, flag4_col)
smartVolNetBuyDiff14 = lambda df: smartVolNetBuyDiff10to14(df, flag5_col)


def smartVolNetBuyDiff15to19(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.compress(df[:, flagCol], df[:, LASTPXCOL])
    resDiff = np.zeros_like(res)
    resDiff[1:] = np.sign(res[1:] - res[:-1])
    if np.all(np.isnan(resDiff)):
        return np.nan
    return np.nanmean(resDiff)


smartVolNetBuyDiff15 = lambda df: smartVolNetBuyDiff15to19(df, flag1_col)
smartVolNetBuyDiff16 = lambda df: smartVolNetBuyDiff15to19(df, flag2_col)
smartVolNetBuyDiff17 = lambda df: smartVolNetBuyDiff15to19(df, flag3_col)
smartVolNetBuyDiff18 = lambda df: smartVolNetBuyDiff15to19(df, flag4_col)
smartVolNetBuyDiff19 = lambda df: smartVolNetBuyDiff15to19(df, flag5_col)


def smartVolNetBuyDiff20to24(df, flagCol):
    if len(df) <= 3600:
        return np.nan
    res = np.compress(df[:, flagCol], df[:, LASTPXCOL])
    resDiff = np.zeros_like(res)
    resDiff[1:] = res[1:] - res[:-1]
    if np.all(np.isnan(resDiff)):
        return np.nan
    return normalize(resDiff)


smartVolNetBuyDiff20 = lambda df: smartVolNetBuyDiff20to24(df, flag1_col)
smartVolNetBuyDiff21 = lambda df: smartVolNetBuyDiff20to24(df, flag2_col)
smartVolNetBuyDiff22 = lambda df: smartVolNetBuyDiff20to24(df, flag3_col)
smartVolNetBuyDiff23 = lambda df: smartVolNetBuyDiff20to24(df, flag4_col)
smartVolNetBuyDiff24 = lambda df: smartVolNetBuyDiff20to24(df, flag5_col)
