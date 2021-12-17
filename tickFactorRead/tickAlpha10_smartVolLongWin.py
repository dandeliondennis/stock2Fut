from tickData.tickCsvToAlpha import tickFactorRead




smartVol_win3_0 = {}
PATH_WIN3_0 = 'D://tick_factor//tick_smartVol_win=3_//smartVol_win=3_{}.csv'
i = 27
smartVol_win3_0[i] = tickFactorRead(PATH_WIN3_0.format(i))


smartVol_win6_0 = {}
PATH_WIN6_0 = 'D://tick_factor//tick_smartVol_win=6_//smartVol_win=6_{}.csv'
smartVol_win6_0[i] = tickFactorRead(PATH_WIN6_0.format(i))


smartVol_win9_0 = {}
PATH_WIN9_0 = 'D://tick_factor//tick_smartVol_win=9_//smartVol_win=9_{}.csv'
smartVol_win9_0[i] = tickFactorRead(PATH_WIN9_0.format(i))


smartVol_win15_0 = {}
PATH_WIN15_0 = 'D://tick_factor//tick_smartVol_win=15_//smartVol_win=15_{}.csv'
smartVol_win15_0[i] = tickFactorRead(PATH_WIN15_0.format(i))


smartVol_win30_0 = {}
PATH_WIN30_0 = 'D://tick_factor//tick_smartVol_win=30_//smartVol_win=30_{}.csv'
smartVol_win30_0[i] = tickFactorRead(PATH_WIN30_0.format(i))

