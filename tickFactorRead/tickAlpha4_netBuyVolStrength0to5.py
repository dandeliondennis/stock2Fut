from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_netBuyVolStrength{}//netBuyVolStrength{}.csv'
netBuyVolStrength0 = tickFactorRead(PATH.format(0, 0))
netBuyVolStrength1 = tickFactorRead(PATH.format(1, 1))
netBuyVolStrength2 = tickFactorRead(PATH.format(2, 2))
netBuyVolStrength3 = tickFactorRead(PATH.format(3, 3))
netBuyVolStrength4 = tickFactorRead(PATH.format(4, 4))
netBuyVolStrength5 = tickFactorRead(PATH.format(5, 5))


