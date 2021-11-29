from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_sellBuyAmountDiff{}//sellBuyAmountDiff{}.csv'
sellBuyAmountDiff0 = tickFactorRead(PATH.format(0, 0))
sellBuyAmountDiff1 = tickFactorRead(PATH.format(1, 1))
sellBuyAmountDiff2 = tickFactorRead(PATH.format(2, 2))
sellBuyAmountDiff3 = tickFactorRead(PATH.format(3, 3))
sellBuyAmountDiff4 = tickFactorRead(PATH.format(4, 4))
sellBuyAmountDiff5 = tickFactorRead(PATH.format(5, 5))
sellBuyAmountDiff6 = tickFactorRead(PATH.format(6, 6))

