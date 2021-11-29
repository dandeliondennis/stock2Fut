from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_volAdjustedMom_//volAdjustedMom_{}.csv'
volAdjustedMom_5 = tickFactorRead(PATH.format(5))
volAdjustedMom_6 = tickFactorRead(PATH.format(6))
volAdjustedMom_7 = tickFactorRead(PATH.format(7))
volAdjustedMom_8 = tickFactorRead(PATH.format(8))
volAdjustedMom_9 = tickFactorRead(PATH.format(9))
volAdjustedMom_10 = tickFactorRead(PATH.format(10))

