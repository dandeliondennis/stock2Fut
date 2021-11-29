import numpy as np


S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3


def calcSpread(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 4])
    spread = df[:, S1COL] - df[:, B1COL]
    spread1 = df[:, S1COL]/df[:, B1COL] -1
    spread[spread <= 0] = np.nan
    toS = np.abs(df[:, LASTPXCOL] - df[:, S1COL])
    toB = np.abs(df[:, LASTPXCOL] - df[:, B1COL])
    tmp = np.sign(toS - toB)
    equalSB = np.where(df[:, LASTPXCOL] == df[:, S1COL], 1,
                            np.where(df[:, LASTPXCOL] == df[:, B1COL], -1, 0))
    lastPoint = (df[:, S1COL] - df[:, LASTPXCOL]) / spread - 0.5
    return np.c_[df, spread, spread1, tmp, equalSB, lastPoint]


SPREADCOL = 16
SPREAD1COL = 17
TMPCOL = 18
EQUALHIGHLOWCOL = 19
LASTPOINTCOL = 20


def sellToBuy16(df):
    if df.size == 0:
        return np.nan
    equalHighLow = df[:, EQUALHIGHLOWCOL]
    return np.sum(equalHighLow)


def sellToBuy17(df):
    if df.size == 0:
        return np.nan
    equalHighLow = df[:, EQUALHIGHLOWCOL]
    return np.mean(equalHighLow)


def sellToBuy18(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, SPREADCOL])):
        return np.nan
    tmp = df[:, TMPCOL] * df[:, SPREADCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, SPREADCOL])


def sellToBuy19(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, SPREADCOL])):
        return np.nan
    tmp = df[:, TMPCOL] * df[:, SPREAD1COL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, SPREADCOL])


def sellToBuy20(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, SPREADCOL])):
        return np.nan
    tmp = df[:, EQUALHIGHLOWCOL] * df[:, SPREADCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, SPREADCOL])


def sellToBuy21(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, SPREADCOL])):
        return np.nan
    tmp = df[:, EQUALHIGHLOWCOL] * df[:, SPREADCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, SPREADCOL])


def sellToBuy22(df):
    if df.size == 0:
        return np.nan
    if np.all(np.isnan(df[:, SPREADCOL])):
        return np.nan
    last_point = df[:, LASTPOINTCOL]
    tmp = last_point * df[:, SPREADCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, SPREADCOL])


