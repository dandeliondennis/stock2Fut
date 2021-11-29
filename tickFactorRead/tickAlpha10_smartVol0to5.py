from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVol_//smartVol_{}.csv'
smartVol_0 = tickFactorRead(PATH.format(0))
smartVol_1 = tickFactorRead(PATH.format(1))
smartVol_2 = tickFactorRead(PATH.format(2))
smartVol_3 = tickFactorRead(PATH.format(3))
smartVol_4 = tickFactorRead(PATH.format(4))
smartVol_5 = tickFactorRead(PATH.format(5))

