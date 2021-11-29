import numpy as np

PRICECOL = 3


def calcRet(df):
    if df.size == 0:
        return np.empty([df.shape[0], df.shape[1]+2])
    price = df[:, PRICECOL]
    ret = np.zeros_like(price)
    ret[1:] = np.log(price[1:] / price[:-1])
    volNaN = np.isnan(df[:, VOLCOL])

    return np.c_[df, ret, volNaN]

RETCOL = 15
VOLNANCOL = 16

def tickMom1(df):
    if df.size == 0:
        return np.nan
    return np.nansum(np.sign(df[:, RETCOL]))


def tickMom2(df):
    if df.size == 0:
        return np.nan
    retStd = np.nanstd(df[:, RETCOL])
    thresh = 0.1*retStd
    sign = np.where(df[:, RETCOL]>thresh, 1,
                    np.where(df[:, RETCOL]<-thresh, -1, 0))
    return np.sum(sign)


def tickMom3(df):
    if df.size == 0:
        return np.nan
    retStd = np.nanstd(df[:, RETCOL])
    thresh = 0.25*retStd
    sign = np.where(df[:, RETCOL]>thresh, 1,
                    np.where(df[:, RETCOL]<-thresh, -1, 0))
    return np.sum(sign)


def tickMom4(df):
    if df.size == 0:
        return np.nan
    retStd = np.nanstd(df[:, RETCOL])
    thresh = 0.5*retStd
    sign = np.where(df[:, RETCOL]>thresh, 1,
                    np.where(df[:, RETCOL]<-thresh, -1, 0))
    return np.sum(sign)


VOLCOL = 11
def tickMom5(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    return np.nansum(df[:, VOLCOL] * df[:, RETCOL])/np.nansum(df[:, VOLCOL])


VOLCOL = 11
def tickMom6(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    return np.nansum(df[:, VOLCOL] * np.sign(df[:, RETCOL]))/np.nansum(df[:, VOLCOL])


def tickMom7(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL])*0.25
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * df[:, RETCOL])/(np.sum(realVol) +0.01)


def tickMom8(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL])*0.5
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * df[:, RETCOL])/(np.sum(realVol) + 0.01)


def tickMom9(df):
    if df.size == 0:
        return np.nan
    if np.all(df[:, VOLNANCOL]):
        return np.nan
    volStd = np.nanstd(df[:, VOLCOL])*0.75
    realVol = np.where(df[:, VOLCOL]>volStd, df[:, VOLCOL], 0)
    return np.sum(realVol * df[:, RETCOL])/(np.sum(realVol) + 0.01)


def tickMom10(df):
    if df.size == 0:
        return np.nan

    retStd = np.nanstd(df[:, RETCOL])
    thresh = 0.25*retStd
    truncRet = np.where(np.abs(df[:, RETCOL])>thresh, df[:, RETCOL], 0)
    return np.sum(truncRet)


def tickMom11(df):
    if df.size == 0:
        return np.nan
    retStd = np.nanstd(df[:, RETCOL])
    thresh = 0.5*retStd
    truncRet = np.where(np.abs(df[:, RETCOL])>thresh, df[:, RETCOL], 0)
    return np.sum(truncRet)


