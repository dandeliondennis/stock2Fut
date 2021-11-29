import numpy as np


AVGPRICECOL = 14
S1COL = 6
B1COL = 7
VOLCOL = 11
AMOUNTCOL = 12


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


# common function
def sellAndBuyVol(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1]+3])

    nanIdxS1 = np.isnan(df[:, S1COL])
    nanIdxB1 = np.isnan(df[:, B1COL])
    nanIdxAvgPrice = np.isnan(df[:, AVGPRICECOL])
    nanIdxVol = np.isnan(df[:, VOLCOL])

    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    solveNaNIdx = np.logical_and.reduce([nanIdxS1, nanIdxB1, nanIdxAvgPrice, nanIdxVol])
    sellVol, buyVol = solveVol(s1past, b1past, df[:, AVGPRICECOL], df[:, VOLCOL], solveNaNIdx)
    netBuyVol = sellVol - buyVol
    return np.c_[df, sellVol, buyVol, netBuyVol]


SELLVOLCOL = 15
BUYVOLCOL = 16
NETBUYVOL = 17



# funcSet Function
def rollingNetBuyVolStrength(dfList):
    df = np.vstack(dfList)
    if df.size==0:
        return np.nan
    if np.all(np.isnan(df[:, NETBUYVOL])):
        return np.nan
    netBuyVolReal = df[:, NETBUYVOL]
    thresh = np.nanstd(netBuyVolReal)

    if thresh==0:
        return np.nan
    nNum = df[:, NETBUYVOL]/thresh
    nNum = np.where(np.abs(nNum) > 0.05, nNum, 0)
    return np.nanmean(nNum)
