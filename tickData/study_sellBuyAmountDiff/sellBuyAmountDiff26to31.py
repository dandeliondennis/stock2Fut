import numpy as np
import numba as nb

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
    mid = (df[:, S1COL] + df[:, B1COL])/2
    tmp1 = (df[:, S1COL] - mid) * df[:, SV1COL]
    tmp2 = (mid - df[:, B1COL]) * df[:, BV1COL]

    return np.c_[df, tmp, mid, tmp1, tmp2]


TMPCOL = 16
MIDCOL = 17
TMP1COL = 18
TMP2COL = 19


@nb.njit
def normalize(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i>0:
            pos += i
        elif i<0:
            neg += i
        else:
            pass
    if (pos - neg) ==0:
        return np.nan
    else:
        return (pos + neg)/(pos - neg)


def sellBuyAmountDiff26(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    net = netSell - netBuy
    res = np.zeros_like(net)
    res[1:] = net[1:] - net[:-1]
    if np.all(np.isnan(res)):
        return np.nan
    return normalize(res)


def sellBuyAmountDiff27(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*2
    res1 = np.where(np.abs(res)>thresh, thresh*np.sign(res), res)
    return normalize(res1)


def sellBuyAmountDiff28(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*3
    res1 = np.where(np.abs(res)>thresh, thresh*np.sign(res), res)
    return normalize(res1)


def sellBuyAmountDiff29(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*5
    res1 = np.where(np.abs(res)>thresh, thresh*np.sign(res), res)
    return normalize(res1)


def sellBuyAmountDiff30(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*0.1
    res1 = np.where(np.abs(res)<thresh, 0, res)
    return normalize(res1)


def sellBuyAmountDiff31(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*0.25
    res1 = np.where(np.abs(res)<thresh, 0, res)
    return normalize(res1)


