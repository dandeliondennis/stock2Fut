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
    df[:, S1COL][df[:, S1COL] <= 0] = np.nan
    df[:, B1COL][df[:, B1COL] <= 0] = np.nan
    df[:, SV1COL][df[:, SV1COL] <= 0] = np.nan
    df[:, BV1COL][df[:, BV1COL] <= 0] = np.nan
    s1past = np.roll(df[:, S1COL], 1)
    s1past[0] = np.nan
    b1past = np.roll(df[:, B1COL], 1)
    b1past[0] = np.nan
    s1past_5 = np.roll(df[:, S1COL], 5)
    s1past[0:5] = np.nan
    b1past_5 = np.roll(df[:, B1COL], 5)
    b1past[0:5] = np.nan
    ratio = df[:, BV1COL] / (df[:, BV1COL] + df[:, SV1COL])
    ratioDelta = ratio - np.roll(ratio, 1)
    return np.c_[df, s1past, b1past, b1past_5, s1past_5, ratio, ratioDelta]


S1PASTCOL = 16
S1PAST5COL = 17
B1PASTCOL = 18
B1PAST5COL = 19
RATIOCOL = 20
RATIODELTACOL = 21


def s1b1_11(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, S1COL] - df[:, S1PASTCOL])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_12(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, B1COL] - df[:, B1PASTCOL])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_13(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, S1COL] - df[:, S1PAST5COL])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_14(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, B1COL] - df[:, B1PAST5COL])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_15(df):
    if df.size == 0:
        return np.nan
    tmp = np.sign(df[:, B1COL] - df[:, B1PAST5COL]) + np.sign(df[:, S1COL] - df[:, S1PASTCOL])
    if np.all(np.isnan(tmp)):
        return np.nan
    return np.nanmean(tmp)


def s1b1_16(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, B1COL] * df[:, BV1COL] - df[:, S1COL] * df[:, SV1COL]
    tmpPast5 = np.roll(tmp, 5)
    tmpPast5[:5] = np.nan
    tmpDelta = np.sign(tmp - tmpPast5)
    if np.all(np.isnan(tmpDelta)):
        return np.nan
    return np.nanmean(tmpDelta)


def s1b1_17(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, BV1COL] / (df[:, BV1COL] + df[:, SV1COL])
    tmpPast5 = np.roll(tmp, 5)
    tmpPast5[:5] = np.nan
    tmpDelta = np.sign(tmp - tmpPast5)
    if np.all(np.isnan(tmpDelta)):
        return np.nan
    return np.nanmean(tmpDelta)


def s1b1_18(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, BV1COL] / (df[:, BV1COL] + df[:, SV1COL])
    tmpPast5 = np.roll(tmp, 5)
    tmpPast5[:5] = np.nan
    tmpDelta = np.sign(tmp - tmpPast5) * df[:, VOLCOL]
    if np.all(np.isnan(tmpDelta)):
        return np.nan
    return np.nansum(tmpDelta) / np.sum(df[:, VOLCOL])


def s1b1_19(df):
    if df.size == 0:
        return np.nan
    tmp = df[:, BV1COL] / (df[:, BV1COL] + df[:, SV1COL])
    tmpPast = np.roll(tmp, 1)
    tmpPast[:1] = np.nan
    tmpDelta = tmp - tmpPast
    tmpDeltaStd = np.nanstd(tmpDelta)
    tmpDelta[np.abs(tmpDelta) < (0.25 * tmpDeltaStd)] = 0
    if np.all(np.isnan(tmpDelta)):
        return np.nan
    return np.nanmean(tmpDelta)
