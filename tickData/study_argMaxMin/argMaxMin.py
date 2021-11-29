import numpy as np
import pandas as pd
import numba as nb
from numba import int64, float64

LASTPXCOL = 3
S1COL = 8
B1COL = 9
SV1COL = 10
BV1COL = 11
VOLCOL = 13
AMOUNTCOL = 14



def rowFilter(df):
    nrow, ncol = df.shape
    if nrow <= 3600:
        return np.empty([1, ncol])
    return df


def argMaxMin(df):
    if df.shape[0] <= 1:
        return np.nan
    close = df[:, LASTPXCOL]
    highID, lowID = np.nanargmax(close), np.nanargmin(close)
    return (highID - lowID)/len(close)



