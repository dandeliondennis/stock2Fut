from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_volAdjustedMom_//volAdjustedMom_{}.csv'
volAdjustedMom_0 = tickFactorRead(PATH.format(0))
volAdjustedMom_1 = tickFactorRead(PATH.format(1))
volAdjustedMom_2 = tickFactorRead(PATH.format(2))
volAdjustedMom_3 = tickFactorRead(PATH.format(3))
volAdjustedMom_4 = tickFactorRead(PATH.format(4))

