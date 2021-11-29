from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_sellBuyAmountDiff_//sellBuyAmountDiff_{}.csv'
(sellBuyAmountDiff19, sellBuyAmountDiff20, sellBuyAmountDiff21,
 sellBuyAmountDiff22, sellBuyAmountDiff23, sellBuyAmountDiff24,
 sellBuyAmountDiff25, sellBuyAmountDiff26, sellBuyAmountDiff27,
 sellBuyAmountDiff28, sellBuyAmountDiff29, sellBuyAmountDiff30,
 sellBuyAmountDiff31, sellBuyAmountDiff32, sellBuyAmountDiff33,
 sellBuyAmountDiff34, sellBuyAmountDiff35
 ) = (tickFactorRead(PATH.format(i)) for i in range(19, 36))
