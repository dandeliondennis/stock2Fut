import numpy as np

HIGHCOL = 4
LOWCOL = 5
S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3


def calcSpread(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 4])
    spread = df[:, HIGHCOL] - df[:, LOWCOL]
    spread[spread <= 0] = np.nan
    toHigh = np.abs(df[:, LASTPXCOL] - df[:, HIGHCOL])
    toLow = np.abs(df[:, LASTPXCOL] - df[:, LOWCOL])
    tmp = np.sign(toHigh - toLow)
    equalHighLow = np.where(df[:, LASTPXCOL] == df[:, HIGHCOL], 1,
                            np.where(df[:, LASTPXCOL] == df[:, LOWCOL], -1, 0))
    lastPoint = (df[:, HIGHCOL] - df[:, LASTPXCOL]) / spread - 0.5
    return np.c_[df, spread, tmp, equalHighLow, lastPoint]


SPREADCOL = 16
TMPCOL = 17
EQUALHIGHLOWCOL = 18
LASTPOINTCOL = 19


def highToLow0(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp)


def highToLow1(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def highToLow2(df):
    if df.size == 0:
        return np.nan
    equalHighLow = df[:, EQUALHIGHLOWCOL]
    return np.sum(equalHighLow)


def highToLow3(df):
    if df.size == 0:
        return np.nan
    equalHighLow = df[:, EQUALHIGHLOWCOL]
    return np.mean(equalHighLow)


def highToLow4(df):
    if df.size == 0:
        return np.nan
    lastLast = np.roll(df[:, LASTPXCOL], 1)
    lastLast[0] = np.nan
    increase = (df[:, LASTPXCOL] - lastLast) / df[:, SPREADCOL]
    if np.all(np.isnan(increase)):
        return np.nan
    return np.nanmean(increase)


def highToLow5(df):
    if df.size == 0:
        return np.nan
    lastLast = np.roll(df[:, LASTPXCOL], 1)
    lastLast[0] = np.nan
    increase = (df[:, LASTPXCOL] - lastLast) / df[:, SPREADCOL]
    if np.all(np.isnan(increase)):
        return np.nan
    return np.nansum(increase)


def highToLow6(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL] * df[:, SPREADCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, SPREADCOL])


def highToLow7(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL] * df[:, VOLCOL]
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nansum(tmp) / np.nansum(df[:, VOLCOL])


def highToLow8(df):
    if df.size == 0:
        return np.nan
    increase = df[:, LASTPOINTCOL]
    if np.all(np.isnan(increase)):
        return np.nan
    return np.nansum(increase)


def highToLow9(df):
    if df.size == 0:
        return np.nan
    increase = df[:, LASTPOINTCOL]
    if np.all(np.isnan(increase)):
        return np.nan
    return np.nanmean(increase)


def highToLow10(df):
    if df.size == 0:
        return np.nan
    increase = df[:, LASTPOINTCOL] * df[:, VOLCOL]
    if np.all(np.isnan(increase)):
        return np.nan
    return np.nansum(increase) / np.nansum(df[:, VOLCOL])
