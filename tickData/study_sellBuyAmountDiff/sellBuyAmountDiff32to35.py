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
    mid = (df[:, S1COL] + df[:, B1COL]) / 2
    tmp1 = (df[:, S1COL] - mid) * df[:, SV1COL]
    tmp2 = (mid - df[:, B1COL]) * df[:, BV1COL]

    return np.c_[df, tmp, mid, tmp1, tmp2]


TMPCOL = 16
MIDCOL = 17
TMP1COL = 18
TMP2COL = 19


@nb.njit
def rollingRank(arr, window):
    res = np.zeros_like(arr)
    for i in range(window, len(arr)):
        for j in range(i-window, i):
            if np.isnan(arr[i]) or np.isnan(arr[j]):
                pass
            else:
                res[i] += np.sign(arr[i] - arr[j])
    return res


@nb.njit
def sellBuyAmountDiff32(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    net = netSell - netBuy
    res = rollingRank(net, 2)
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


@nb.njit
def sellBuyAmountDiff33(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    net = netSell - netBuy
    res = rollingRank(net, 5)
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


@nb.njit
def sellBuyAmountDiff34(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    net = netSell - netBuy
    res = np.zeros_like(net)
    res[2:] = np.sign(net[2:] - net[:-2])
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


@nb.njit
def sellBuyAmountDiff35(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    net = netSell - netBuy
    res = np.zeros_like(net)
    res[3:] = np.sign(net[3:] - net[:-3])
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)