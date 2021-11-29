from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVolNetBuyDiff_//smartVolNetBuyDiff_{}.csv'
(smartVolNetBuyDiff10, smartVolNetBuyDiff11,
 smartVolNetBuyDiff12, smartVolNetBuyDiff13,
 smartVolNetBuyDiff14, smartVolNetBuyDiff15,
 smartVolNetBuyDiff16, smartVolNetBuyDiff17,
 smartVolNetBuyDiff18, smartVolNetBuyDiff19,
 smartVolNetBuyDiff20, smartVolNetBuyDiff21,
 smartVolNetBuyDiff22, smartVolNetBuyDiff23,
 smartVolNetBuyDiff24,
 ) = (tickFactorRead(PATH.format(i)) for i in range(10, 25))
