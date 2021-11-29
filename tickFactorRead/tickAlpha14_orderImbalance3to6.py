from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_orderImbalance_//orderImbalance_{}.csv'

(orderImbalance_3, orderImbalance_4,
 orderImbalance_5, orderImbalance_6) = (tickFactorRead(PATH.format(i)) for i in range(3, 7))