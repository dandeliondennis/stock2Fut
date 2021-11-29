from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_sellBuyAmountDiff_//sellBuyAmountDiff_{}.csv'
(sellBuyAmountDiff40, sellBuyAmountDiff41,
 sellBuyAmountDiff42, sellBuyAmountDiff43,
 sellBuyAmountDiff44, sellBuyAmountDiff45,
 sellBuyAmountDiff46,
 ) = (tickFactorRead(PATH.format(i)) for i in range(40, 47))
