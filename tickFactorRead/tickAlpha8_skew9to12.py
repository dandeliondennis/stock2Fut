from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_skew_//skew_{}.csv'
skew_9 = tickFactorRead(PATH.format(9))
skew_10 = tickFactorRead(PATH.format(10))
skew_11 = tickFactorRead(PATH.format(11))
skew_12 = tickFactorRead(PATH.format(12))

