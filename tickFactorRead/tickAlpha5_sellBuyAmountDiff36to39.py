from tickData.tickCsvToAlpha import tickFactorRead

PATH = 'D://tick_factor//tick_sellBuyAmountDiff_//sellBuyAmountDiff_{}.csv'
(sellBuyAmountDiff36, sellBuyAmountDiff37,
 sellBuyAmountDiff38, sellBuyAmountDiff39) = (tickFactorRead(PATH.format(i)) for i in range(36, 40))
