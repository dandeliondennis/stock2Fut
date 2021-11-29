import numpy as np


S1COL = 6
B1COL = 7
VOLCOL = 11
SV1COL = 8
BV1COL = 9
LASTPXCOL = 3

def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1]+3])
    volNaN = np.isnan(df[:, VOLCOL])
    lastPriceNext = np.roll(df[:, LASTPXCOL], -1)
    lastPriceNext[-1] = np.nan

    spread = df[:, S1COL] - df[:, B1COL]
    spread = np.where(spread==0, np.nan, spread)
    return np.c_[df, volNaN, lastPriceNext, spread]

VOLNANCOL = 15
LASTNEXTCOL = 16
SPREADCOL = 17

def avgSellToBuy0(df):
    if df.size == 0:
        return np.nan
    toSell = np.abs(df[:, LASTNEXTCOL] - df[:, S1COL])
    toBuy = np.abs(df[:, LASTNEXTCOL] - df[:, B1COL])
    tmp = np.sign(toSell - toBuy)
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def avgSellToBuy1(df):
    if df.size == 0:
        return np.nan
    point = (df[:, LASTNEXTCOL] - df[:, B1COL])/df[:, SPREADCOL]
    point -= 0.5
    if np.all(np.isnan(point)):
        return np.nan
    return np.nanmean(point)


def avgSellToBuy2(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    toSell = np.abs(df[:, LASTNEXTCOL] - df[:, S1COL])
    toBuy = np.abs(df[:, LASTNEXTCOL] - df[:, B1COL])
    tmp = np.sign(toSell - toBuy)
    return np.nansum(tmp*df[:, VOLCOL])/ np.nansum(df[:, VOLCOL])


def avgSellToBuy3(df):
    if df.size == 0:
        return np.nan
    point = (df[:, LASTNEXTCOL] - df[:, B1COL])/df[:, SPREADCOL]
    point -= 0.5
    point = np.where(np.abs(point)<0.1, 0, point)
    return np.mean(point)


def avgSellToBuy4(df):
    if df.size == 0:
        return np.nan
    point = (df[:, LASTNEXTCOL] - df[:, B1COL])/df[:, SPREADCOL]
    point -= 0.5
    point = np.where(np.abs(point)<0.25, 0, point)
    return np.mean(point)


def avgSellToBuy5(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    point = (df[:, LASTNEXTCOL] - df[:, B1COL])/df[:, SPREADCOL]
    point -= 0.5
    return np.nansum(point*df[:, VOLCOL])/ np.nansum(df[:, VOLCOL])






