from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_S1B1//S1B1{}.csv'
S1B1_5 = tickFactorRead(PATH.format(5))
S1B1_6 = tickFactorRead(PATH.format(6))
S1B1_7 = tickFactorRead(PATH.format(7))
S1B1_8 = tickFactorRead(PATH.format(8))
S1B1_9 = tickFactorRead(PATH.format(9))
S1B1_10 = tickFactorRead(PATH.format(10))