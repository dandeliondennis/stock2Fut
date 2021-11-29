from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_microstructure_//microstructure_{}.csv'
s1Ratio = tickFactorRead(PATH.format(0))
b1Ratio = tickFactorRead(PATH.format(1))
s1Ratio1 = tickFactorRead(PATH.format(2))
b1Ratio1 = tickFactorRead(PATH.format(3))
skew = tickFactorRead(PATH.format(4))
kurtosis = tickFactorRead(PATH.format(5))
tjd = tickFactorRead(PATH.format(6))
spread = tickFactorRead(PATH.format(7))

