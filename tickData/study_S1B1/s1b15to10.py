import numpy as np

S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3


def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 4])
    df[:, S1COL][df[:, S1COL] <= 0] = np.nan
    df[:, B1COL][df[:, B1COL] <= 0] = np.nan
    df[:, SV1COL][df[:, SV1COL] <= 0] = np.nan
    df[:, BV1COL][df[:, BV1COL] <= 0] = np.nan
    s1past = np.roll(df[:, S1COL], 1)
    s1past[0] = np.nan
    b1past = np.roll(df[:, B1COL], 1)
    b1past[0] = np.nan
    tmp = np.sign(df[:, S1COL] - s1past) + np.sign(df[:, B1COL] - b1past)
    ratio = df[:, BV1COL] / (df[:, BV1COL] + df[:, SV1COL])
    return np.c_[df, s1past, b1past, tmp, ratio]


S1PASTCOL = 16
B1PASTCOL = 17
TMPCOL = 18
RATIOCOL = 19


def s1b1_5(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    ratio = df[:, RATIOCOL]
    ratioDelta = ratio - np.roll(ratio, 1)
    ratioDelta[0] = np.nan
    tmp = np.where(tmp == 0, -ratioDelta, tmp)
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_6(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    ratio = df[:, RATIOCOL]
    ratioDelta = ratio - np.roll(ratio, 1)
    ratioDelta[0] = np.nan
    tmp = tmp + ratioDelta
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_7(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]
    ratio = df[:, RATIOCOL]
    ratioDelta = ratio - np.roll(ratio, 1)
    ratioDelta[0] = np.nan
    tmp = tmp - ratioDelta
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_8(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, TMPCOL]/ 2
    tmp = np.where(tmp < 0, tmp - 1,
                   np.where(tmp > 0, tmp + 1, 0))
    ratio = df[:, RATIOCOL]
    ratioDelta = ratio - np.roll(ratio, 1)
    ratioDelta[0] = np.nan
    tmp += ratioDelta
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_9(df):
    if df.size == 0:
        return np.nan
    tmp = (df[:, S1COL] - df[:, B1COL])*(df[:, BV1COL] - df[:, SV1COL])
    tmpPast = np.roll(tmp, 1)
    tmpPast[0] = np.nan
    tmpDelta = np.sign(tmp - tmpPast)
    if np.all(np.isnan(tmpDelta)):
        return np.nan
    return np.nanmean(tmpDelta)


def s1b1_10(df):
    if df.size == 0:
        return np.nan
    ratio = df[:, RATIOCOL]
    ratioDelta = ratio - np.roll(ratio, 1)
    ratioDelta[0] = np.nan
    ratioDelta = np.sign(ratioDelta)
    if np.all(np.isnan(ratioDelta)):
        return np.nan
    return np.nanmean(ratioDelta)