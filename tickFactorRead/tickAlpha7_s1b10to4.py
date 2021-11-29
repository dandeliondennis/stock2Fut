from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_S1B1//S1B1{}.csv'
S1B1_0 = tickFactorRead(PATH.format(0))
S1B1_1 = tickFactorRead(PATH.format(1))
S1B1_2 = tickFactorRead(PATH.format(2))
S1B1_3 = tickFactorRead(PATH.format(3))
S1B1_4 = tickFactorRead(PATH.format(4))
