import numpy as np

LASTPXCOL = 3
S1COL = 6
B1COL = 7
VOLCOL = 11
AMOUNTCOL = 12
SV1COL = 8
BV1COL = 9


def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1]+4])
    volNaN = np.isnan(df[:, VOLCOL])
    lastPriceNext = np.roll(df[:, LASTPXCOL], -1)
    lastPriceNext[-1] = np.nan

    spread = df[:, S1COL] - df[:, B1COL]
    spread = np.where(spread==0, np.nan, spread)
    toSell = np.abs(lastPriceNext - df[:, S1COL])
    toBuy = np.abs(lastPriceNext - df[:, B1COL])
    tmp = np.sign(toSell - toBuy)
    return np.c_[df, volNaN, lastPriceNext, spread, tmp]


VOLNANCOL = 15
LASTNEXTCOL = 16
SPREADCOL = 17
TMPCOL = 18


def avgSellToBuy6(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    return np.nansum(tmp*df[:, VOLCOL])/ np.nansum(df[:, VOLCOL])


def avgSellToBuy7(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    return np.nansum(tmp*df[:, AMOUNTCOL])/ np.nansum(df[:, AMOUNTCOL])


def avgSellToBuy8(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    return np.nansum(df[:, VOLCOL]**2*tmp)/ np.nansum(df[:, VOLCOL]**2)


def avgSellToBuy9(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    return np.nansum(df[:, AMOUNTCOL]**2*tmp)/ np.nansum(df[:, AMOUNTCOL]**2)


def avgSellToBuy10(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    volStd = np.nanstd(df[:, VOLCOL])*0.25
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)
    return np.nansum(tmp*realVol)/ np.sum(realVol)


def avgSellToBuy11(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    volStd = np.nanstd(df[:, VOLCOL])*0.5
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)
    return np.nansum(tmp*realVol)/ np.sum(realVol)


def avgSellToBuy12(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    volStd = np.nanstd(df[:, VOLCOL])*0.75
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)
    return np.nansum(tmp*realVol)/ np.sum(realVol)


def avgSellToBuy13(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    volStd = np.nanstd(df[:, VOLCOL])*0.25
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)**2
    return np.nansum(tmp*realVol)/ np.sum(realVol)


def avgSellToBuy14(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    volStd = np.nanstd(df[:, VOLCOL])*0.5
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)**2
    return np.nansum(tmp*realVol)/ np.sum(realVol)


def avgSellToBuy15(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    if np.all(np.isnan(df[:, TMPCOL])):
        return np.nan
    tmp = np.maximum(df[:, TMPCOL], 0)
    volStd = np.nanstd(df[:, VOLCOL])*0.75
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)**2
    return np.nansum(tmp*realVol)/ np.sum(realVol)
