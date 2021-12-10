from tickData.tickCsvToAlpha import tickFactorRead

smartDistanceDict0 = {}
PATH0 = 'D://tick_factor//tick_smartDistance_//smartDistance_0_{}.csv'
for i in range(0, 4):
    smartDistanceDict0[i] = tickFactorRead(PATH0.format(i))

smartDistanceDict1 = {}
PATH1 = 'D://tick_factor//tick_smartDistance_//smartDistance_1_{}.csv'
for i in range(0, 4):
    smartDistanceDict1[i] = tickFactorRead(PATH1.format(i))

smartDistanceDict2 = {}
PATH2 = 'D://tick_factor//tick_smartDistance_//smartDistance_2_{}.csv'
for i in range(0, 8):
    smartDistanceDict2[i] = tickFactorRead(PATH2.format(i))
