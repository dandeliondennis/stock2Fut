from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_orderImbalance_//orderImbalance_{}.csv'

(orderImbalance1, orderImbalance2) = (tickFactorRead(PATH.format(i)) for i in range(1, 3))