from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVol_//smartVol_{}.csv'
smartVol_12 = tickFactorRead(PATH.format(12))
smartVol_13 = tickFactorRead(PATH.format(13))
smartVol_14 = tickFactorRead(PATH.format(14))
smartVol_15 = tickFactorRead(PATH.format(15))
smartVol_16 = tickFactorRead(PATH.format(16))
smartVol_17 = tickFactorRead(PATH.format(17))

