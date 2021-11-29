from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_avgSellToBuy{}//avgSellToBuy{}.csv'
avgSellToBuy0 = tickFactorRead(PATH.format(0, 0))
avgSellToBuy1 = tickFactorRead(PATH.format(1, 1))
avgSellToBuy2 = tickFactorRead(PATH.format(2, 2))
avgSellToBuy3 = tickFactorRead(PATH.format(3, 3))
avgSellToBuy4 = tickFactorRead(PATH.format(4, 4))
avgSellToBuy5 = tickFactorRead(PATH.format(5, 5))


