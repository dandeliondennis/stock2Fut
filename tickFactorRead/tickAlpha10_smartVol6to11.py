from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVol_//smartVol_{}.csv'
smartVol_6 = tickFactorRead(PATH.format(6))
smartVol_7 = tickFactorRead(PATH.format(7))
smartVol_8 = tickFactorRead(PATH.format(8))
smartVol_9 = tickFactorRead(PATH.format(9))
smartVol_10 = tickFactorRead(PATH.format(10))
smartVol_11 = tickFactorRead(PATH.format(11))

