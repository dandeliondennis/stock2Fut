import numpy as np

S1COL = 8
B1COL = 9
VOLCOL = 13
SV1COL = 10
BV1COL = 11
LASTPXCOL = 3


def calcVolNaN(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1] + 2])
    df[:, S1COL][df[:, S1COL] <=0] = np.nan
    df[:, B1COL][df[:, B1COL] <= 0] = np.nan
    df[:, SV1COL][df[:, SV1COL] <=0] = np.nan
    df[:, BV1COL][df[:, BV1COL] <= 0] = np.nan
    s1past = np.roll(df[:, S1COL], 1)
    s1past[0] = np.nan
    b1past = np.roll(df[:, B1COL], 1)
    b1past[0] = np.nan
    return np.c_[df, s1past, b1past]


S1PASTCOL = 16
B1PASTCOL = 17


def s1b1_0(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, S1COL] - df[:, S1PASTCOL]) + np.sign(df[:, B1COL] - df[:, B1PASTCOL])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_1(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, S1COL] / df[:, S1PASTCOL] - 1 + df[:, B1COL] / df[:, B1PASTCOL] - 1
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_2(df):
    if df.size == 0:
        return np.nan
    s1Delta = df[:, S1COL] - df[:, S1PASTCOL]
    b1Delta = df[:, B1COL] - df[:, B1PASTCOL]
    if np.all(np.isnan(s1Delta)) or np.all(np.isnan(b1Delta)):
        return np.nan
    s1DeltaTotal = np.nansum(np.abs(s1Delta))
    b1DeltaTotal = np.nansum(np.abs(b1Delta))
    if s1DeltaTotal <= 0 or b1DeltaTotal <= 0:
        return np.nan
    tmp1 = np.nansum(np.maximum(s1Delta, 0)) / s1DeltaTotal - .5
    tmp2 = np.nansum(np.maximum(b1Delta, 0)) / b1DeltaTotal - .5
    return tmp1 + tmp2


def s1b1_3(df):
    if df.size == 0:
        return np.nan
    tmp1 = np.minimum(df[:, S1COL] / df[:, B1PASTCOL] -1, 0)
    tmp2 = np.maximum(df[:, B1COL] / df[:, S1PASTCOL] -1, 0)
    tmp = tmp1 + tmp2
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_4(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, S1COL] - df[:, S1PASTCOL]) + np.sign(df[:, B1COL] - df[:, B1PASTCOL])

    ratio = df[:, BV1COL] / (df[:, BV1COL] + df[:, SV1COL])
    ratioDelta = ratio - np.roll(ratio, 1)
    ratioDelta[0] = np.nan
    tmp = np.where(tmp == 0, ratioDelta, tmp)
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)
