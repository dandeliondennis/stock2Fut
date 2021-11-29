from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_sellBuyAmountDiff_//sellBuyAmountDiff_{}.csv'
(sellBuyAmountDiff7, sellBuyAmountDiff8, sellBuyAmountDiff9,
 sellBuyAmountDiff10, sellBuyAmountDiff11, sellBuyAmountDiff12,
 sellBuyAmountDiff13, sellBuyAmountDiff14, sellBuyAmountDiff15,
 sellBuyAmountDiff16, sellBuyAmountDiff17, sellBuyAmountDiff18) = (tickFactorRead(PATH.format(i)) for i in range(7, 19))
