from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_smartVolNetBuyDiff_//smartVolNetBuyDiff_{}.csv'
(smartVolNetBuyDiff25,
 smartVolNetBuyDiff26, smartVolNetBuyDiff27,
 smartVolNetBuyDiff28, smartVolNetBuyDiff29,
 smartVolNetBuyDiff30, smartVolNetBuyDiff31,
 smartVolNetBuyDiff32, smartVolNetBuyDiff33,
 smartVolNetBuyDiff34,
 ) = (tickFactorRead(PATH.format(i)) for i in range(25, 35))
