from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_argMaxMin_//argMaxMin_{}.csv'
(argMaxMin0,
 ) = (tickFactorRead(PATH.format(i)) for i in range(0, 1))
