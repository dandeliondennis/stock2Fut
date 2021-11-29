import numpy as np


S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3


def solve(s1, b1, avg_price, vol, nanID):
    if nanID:
        return np.nan, np.nan
    if (vol < 1e-2) or (avg_price < 1e-2):
        svol, bvol = 0., 0.
        return svol, bvol
    coef = np.array([[s1 - avg_price, b1 - avg_price], [1.0, 1.0]])
    const = np.array([0.0, vol])
    try:
        svol, bvol = np.linalg.solve(coef, const)
        return svol, bvol
    except:
        svol, bvol = np.nan, np.nan
        return svol, bvol


solveVol = np.vectorize(solve)


def sellAndBuyVol(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1]+5])
    s1past = np.roll(df[:, S1COL], 1)
    s1past[0] = np.nan
    b1past = np.roll(df[:, B1COL], 1)
    b1past[0] = np.nan

    nanIdxS1 = np.isnan(s1past)
    nanIdxB1 = np.isnan(b1past)
    nanIdxLastPrice = np.isnan(df[:, LASTPXCOL])
    nanIdxVol = np.isnan(df[:, VOLCOL])
    solveNaNIdx = np.logical_and.reduce([nanIdxS1, nanIdxB1, nanIdxLastPrice, nanIdxVol])
    sellVol, buyVol = solveVol(s1past, b1past, df[:, LASTPXCOL], df[:, VOLCOL], solveNaNIdx)
    return np.c_[df, s1past, b1past, sellVol, buyVol, nanIdxVol]



S1PASTCOL = 16
B1PASTCOL = 17
SELLVOLCOL = 18
BUYVOLCOL = 19
VOLNANCOL = 20


def avgSellToBuy0(df):
    if df.size == 0:
        return np.nan
    toSell = np.abs(df[:, LASTPXCOL] - df[:, S1PASTCOL])
    toBuy = np.abs(df[:, LASTPXCOL] - df[:, B1PASTCOL])
    tmp = np.sign(toSell - toBuy)
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp)


def netBuyVolStrength0(df):
    if df.size == 0:
        return np.nan
    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = buyVol - sellVol
    return np.nansum(np.sign(netBuyVol))