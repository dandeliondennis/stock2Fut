import numpy as np

LASTCOL = 3
HIGHCOL = 4
LOWCOL = 5
S1COL = 8
B1COL = 9
VOLCOL = 13
AMOUNTCOL = 14
OICOL = 12


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
        return np.empty([df.shape[0], df.shape[1]+3])
    s1past = np.roll(df[:, S1COL], 1)
    s1past[0] = np.nan
    b1past = np.roll(df[:, B1COL], 1)
    b1past[0] = np.nan

    nanIdxS1 = np.isnan(s1past)
    nanIdxB1 = np.isnan(b1past)
    nanIdxHighPrice = np.isnan(df[:, HIGHCOL])
    nanIdxLowPrice = np.isnan(df[:, LOWCOL])
    nanIdxVol = np.isnan(df[:, VOLCOL])
    solveNaNIdx = np.logical_and.reduce([nanIdxS1, nanIdxB1, nanIdxHighPrice, nanIdxLowPrice, nanIdxVol])
    avgPrice = 0.5 * (df[:, HIGHCOL] + df[:, LOWCOL])
    sellVol, buyVol = solveVol(s1past, b1past, avgPrice, df[:, VOLCOL], solveNaNIdx)
    return np.c_[df, sellVol, buyVol, nanIdxVol]


SELLVOLCOL = 16
BUYVOLCOL = 17
VOLNANCOL = 18


def netBuyVolStrength0(df):
    if df.size == 0:
        return np.nan
    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = buyVol - sellVol
    netBuyVol = netBuyVol[~netVolNaN]
    return np.sum(np.sign(netBuyVol))


def netBuyVolStrength1(df):
    if df.size == 0:
        return np.nan
    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = (buyVol - sellVol) / df[:, VOLCOL] - .5
    netBuyVol = netBuyVol[~netVolNaN]
    return np.sum(netBuyVol)


def netBuyVolStrength2(df):
    if df.size == 0:
        return np.nan
    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = (buyVol - sellVol) / df[:, VOLCOL] - .5
    netBuyVol = netBuyVol[~netVolNaN]
    thresh = np.std(netBuyVol)*0.25
    netBuyVol[netBuyVol<thresh] = 0
    return np.sum(netBuyVol)


def netBuyVolStrength3(df):
    if df.size == 0:
        return np.nan
    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = (buyVol - sellVol) / df[:, VOLCOL] - .5
    netBuyVol = netBuyVol[~netVolNaN]
    thresh = np.std(netBuyVol)*0.5
    netBuyVol[netBuyVol<thresh] = 0
    return np.sum(netBuyVol)


def netBuyVolStrength4(df):
    if df.size == 0:
        return np.nan
    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = (buyVol - sellVol) / df[:, VOLCOL] - .5
    netBuyVol = netBuyVol[~netVolNaN]
    thresh = np.std(netBuyVol)*0.75
    netBuyVol[netBuyVol<thresh] = 0
    return np.sum(netBuyVol)


def netBuyVolStrength5(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volSum = np.sum(df[:, VOLCOL][~df[:, VOLNANCOL].astype(bool)])
    if volSum == 0:
        return np.nan

    sellVol, buyVol = df[:, SELLVOLCOL], df[:, BUYVOLCOL]
    sellVolNaNIdx, buyVolNaNIdx = np.isnan(sellVol), np.isnan(buyVol)
    netVolNaN = np.logical_or(sellVolNaNIdx, buyVolNaNIdx)
    if np.all(netVolNaN):
        return np.nan
    netBuyVol = buyVol - sellVol
    netBuyVol = netBuyVol[~netVolNaN]
    return np.sum(netBuyVol) / volSum

