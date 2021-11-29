from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_volDownSample_//volDownSample_{}.csv'
(volDownSample0, volDownSample1,
 volDownSample2, volDownSample3,
 ) = (tickFactorRead(PATH.format(i)) for i in range(0, 4))
