from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_skew_//skew_{}.csv'
skew_0 = tickFactorRead(PATH.format(0))
skew_1 = tickFactorRead(PATH.format(1))
skew_2 = tickFactorRead(PATH.format(2))
skew_3 = tickFactorRead(PATH.format(3))
skew_4 = tickFactorRead(PATH.format(4))
skew_5 = tickFactorRead(PATH.format(5))
skew_6 = tickFactorRead(PATH.format(6))
skew_7 = tickFactorRead(PATH.format(7))
skew_8 = tickFactorRead(PATH.format(8))
