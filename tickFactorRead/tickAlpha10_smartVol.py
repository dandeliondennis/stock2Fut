from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVol_//smartVol_{}.csv'
smartVol_18 = tickFactorRead(PATH.format(18))
smartVol_19 = tickFactorRead(PATH.format(19))
smartVol_20 = tickFactorRead(PATH.format(20))
smartVol_21 = tickFactorRead(PATH.format(21))
smartVol_22 = tickFactorRead(PATH.format(22))
smartVol_23 = tickFactorRead(PATH.format(23))
smartVolDict = {}
for i in range(24, 31):
    smartVolDict[i] = tickFactorRead(PATH.format(i))

smartVolDict9 = {}
PATH9 = 'D://tick_factor//tick_smartVol_//smartVol_27_{}.csv'
for i in range(0, 5):
    smartVolDict9[i] = tickFactorRead(PATH9.format(i))

smartVolDict1 = {}
PATH1 = 'D://tick_factor//tick_smartVol_//smartVol_28_{}.csv'
for i in range(0, 5):
    smartVolDict1[i] = tickFactorRead(PATH1.format(i))


smartVolDict2 = {}
PATH2 = 'D://tick_factor//tick_smartVol_//smartVol_29_{}.csv'
for i in range(0, 5):
    smartVolDict2[i] = tickFactorRead(PATH2.format(i))

'''
smartVolDict0 = {}
PATH0 = 'D://tick_factor//tick_smartVol_//smartVol_12_{}.csv'
for i in range(0, 5):
    smartVolDict2[i] = tickFactorRead(PATH0.format(i))

smartVol_12_test = tickFactorRead('D://tick_factor//tick_smartVol_//smartVol_12_test.csv')
'''
smartVol_27_test = tickFactorRead('D://tick_factor//tick_smartVol_//smartVol_27_test.csv')
smartVol_28_test = tickFactorRead('D://tick_factor//tick_smartVol_//smartVol_28_test.csv')
smartVol_29_test = tickFactorRead('D://tick_factor//tick_smartVol_//smartVol_29_test.csv')