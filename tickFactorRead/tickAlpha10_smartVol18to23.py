from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVol_//smartVol_{}.csv'
smartVol_18 = tickFactorRead(PATH.format(18))
smartVol_19 = tickFactorRead(PATH.format(19))
smartVol_20 = tickFactorRead(PATH.format(20))
smartVol_21 = tickFactorRead(PATH.format(21))
smartVol_22 = tickFactorRead(PATH.format(22))
smartVol_23 = tickFactorRead(PATH.format(23))

