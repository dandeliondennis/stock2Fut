import numpy as np
import numba as nb


AVGPRICECOL = 13
S1COL = 5
B1COL = 6
VOLCOL = 10
AMOUNTCOL = 11

@nb.njit
def solveVol(s1, b1, avg_price, vol):
    coef = np.array([[s1 - avg_price, b1 - avg_price], [1.0, 1.0]])
    const = np.array([0, vol])
    try:
        svol, bvol = np.linalg.solve(coef, const)
        return svol, bvol
    except:
        return np.nan, np.nan


vsolve = np.vectorize(solveVol)


def buyVolStrength(df):
    if df.size == 0:
        return np.nan
    s1past = np.roll(df[:, S1COL], 1)
    b1past = np.roll(df[:, B1COL], 1)
    sellVol, buyVol = vsolve(s1past, b1past, df[:, AVGPRICECOL], df[:, VOLCOL] )
    netBuyVol = buyVol - sellVol
    return np.nanmean(netBuyVol)/(np.nanstd(netBuyVol) + 0.01)


def splitData(datalist):
    if len(datalist) >= 1:
        return datalist[-1]
    else:
        return None


def calcNetBuyVolStrength(datalist):
    tmp = splitData(datalist)
    if tmp.size>0:
        return buyVolStrength(tmp)
    else:
        return np.nan
