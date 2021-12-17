from tickData.tickCsvToAlpha import tickFactorRead

smallVolNoise0 = {}

PATH0 = 'D://tick_factor//tick_smallVolNoise_//smallVolNoise_0_{}.csv'
for i in range(0, 13):
    smallVolNoise0[i] = tickFactorRead(PATH0.format(i))


smallVolNoise_win3_0 = {}
name = 'smallVolNoise'
PATH_WIN3_0 = 'D://tick_factor//tick_smallVolNoise_win=3_//smallVolNoise_win=3_0_{}.csv'
for i in range(0, 17):
    smallVolNoise_win3_0[i] = tickFactorRead(PATH_WIN3_0.format(i))


smallVolNoise_win6_0 = {}
name = 'smallVolNoise'
PATH_WIN6_0 = 'D://tick_factor//tick_smallVolNoise_win=6_//smallVolNoise_win=6_0_{}.csv'
for i in range(8, 17):
    smallVolNoise_win6_0[i] = tickFactorRead(PATH_WIN6_0.format(i))


smallVolNoise_win9_0 = {}
name = 'smallVolNoise'
PATH_WIN9_0 = 'D://tick_factor//tick_smallVolNoise_win=9_//smallVolNoise_win=9_0_{}.csv'
for i in range(8, 17):
    smallVolNoise_win9_0[i] = tickFactorRead(PATH_WIN9_0.format(i))


smallVolNoise_win15_0 = {}
name = 'smallVolNoise'
PATH_WIN15_0 = 'D://tick_factor//tick_smallVolNoise_win=15_//smallVolNoise_win=15_0_{}.csv'
for i in range(8, 17):
    smallVolNoise_win15_0[i] = tickFactorRead(PATH_WIN15_0.format(i))


smallVolNoise_win30_0 = {}
name = 'smallVolNoise'
PATH_WIN30_0 = 'D://tick_factor//tick_smallVolNoise_win=30_//smallVolNoise_win=30_0_{}.csv'
for i in range(11, 16):
    smallVolNoise_win30_0[i] = tickFactorRead(PATH_WIN30_0.format(i))

