import numpy as np

VOLCOL = 10
TIMEDELTACOL = 12


def ddRatio(df):
    if df.size == 0:
        return np.nan

    tmp = np.where(df[:, TIMEDELTACOL] == 0, 0, df[:, VOLCOL]/df[:, TIMEDELTACOL])
    volumeMean, volumeStd = np.nanmean(tmp), np.nanstd(tmp)
    bigVolumeLimit = volumeMean + 1.5*volumeStd
    sign = np.where((df[:, VOLCOL]/df[:, TIMEDELTACOL])>bigVolumeLimit, 1, 0)
    return np.nansum(df[:, VOLCOL]*sign)/(np.nansum(df[:, VOLCOL]) + 0.01)








