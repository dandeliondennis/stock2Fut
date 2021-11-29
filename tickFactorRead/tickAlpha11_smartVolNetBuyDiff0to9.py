from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVolNetBuyDiff_//smartVolNetBuyDiff_{}.csv'
(smartVolNetBuyDiff0, smartVolNetBuyDiff1,
 smartVolNetBuyDiff2, smartVolNetBuyDiff3,
 smartVolNetBuyDiff4, smartVolNetBuyDiff5,
 smartVolNetBuyDiff6, smartVolNetBuyDiff7,
 smartVolNetBuyDiff8, smartVolNetBuyDiff9,
 ) = (tickFactorRead(PATH.format(i)) for i in range(0, 10))
