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
    mid = (df[:, S1COL] + df[:, B1COL])/2
    tmp1 = (df[:, S1COL] - mid) * df[:, SV1COL]
    tmp2 = (mid - df[:, B1COL]) * df[:, BV1COL]

    return np.c_[df, tmp, mid, tmp1, tmp2]


TMPCOL = 16
MIDCOL = 17
TMP1COL = 18
TMP2COL = 19


def sellBuyAmountDiff19(df):
    if len(df) <= 3600:
        return np.nan
    tmp = df[:, TMPCOL]
    res = np.zeros(tmp.shape)
    res[1:] = np.sign(tmp[1:] - tmp[:-1])
    if np.all(np.isnan(res)):
        return np.nan
    return np.nansum(res)


def sellBuyAmountDiff20(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = np.sign(netSell - netBuy)
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(res)


def sellBuyAmountDiff21(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    if np.all(np.isnan(netSell)) or np.all(np.isnan(netBuy)):
        return np.nan
    netSellTotal = np.nansum(netSell)
    netBuyTotal = np.nansum(netBuy)
    return (netSellTotal - netBuyTotal)/(netSellTotal + netBuyTotal + 0.001)


def sellBuyAmountDiff22(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    net = netSell - netBuy
    res = np.zeros_like(net)
    res[1:] = net[1:] - net[:-1]
    if np.all(np.isnan(res)):
        return np.nan
    return np.nanmean(np.sign(res))


def sellBuyAmountDiff23(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*0.25
    res[np.abs(res)<thresh] = 0
    return np.nanmean(res)


def sellBuyAmountDiff24(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*0.5
    res[np.abs(res)<thresh] = 0
    return np.nanmean(res)


def sellBuyAmountDiff25(df):
    if len(df) <= 3600:
        return np.nan
    netSell = df[:, TMP1COL]
    netBuy = df[:, TMP2COL]
    res = netSell - netBuy
    if np.all(np.isnan(res)):
        return np.nan
    thresh = np.nanstd(res)*0.75
    res[np.abs(res)<thresh] = 0
    return np.nanmean(res)


