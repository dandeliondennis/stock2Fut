from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_orderImbalance_//orderImbalance_{}.csv'

(orderImbalance0, orderImbalance1) = (tickFactorRead(PATH.format(i)) for i in range(0, 2))