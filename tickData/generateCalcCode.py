name = 'orderImbalance'
start = 3
end = 6
preCalcFunc = 'calcVolDiff'

factorFuncListInit = '{}_{}, '
factorFuncList = ''.join((factorFuncListInit.format(name, idx) for idx in range(start, end + 1)))
factorCalcList = ''.join((factorFuncListInit.format('factorCalcFunc', idx) for idx in range(start, end + 1)))
path = 'D:/Backtest/tickData/'
path_save = 'D:/tick_factor/'

with open(path + 'mainFactor.txt', 'w') as dst:
    with open(path + 'sourceCode1.txt', 'r') as src1:
        src = src1.readlines()
        for sentence in src:
            dst.write(sentence.format(name=name,
                                      start=start,
                                      end=end,
                                      preCalcFunc=preCalcFunc,
                                      factorFuncList=factorFuncList))
    with open(path + 'sourceCode2.txt', 'r') as src2:
        for idx in range(start, end + 1):
            src = src2.readlines()
            src2.seek(0)
            for sentence in src:
                dst.write(sentence.format(idx=idx,
                                          name=name))
    with open(path + 'sourceCode3.txt', 'r') as src3:
        src = src3.readlines()
        for sentence in src:
            dst.write(sentence.format(name=name,
                                      start=start,
                                      end=end,
                                      end_1=end + 1,
                                      factorCalcList=factorCalcList))
    with open(path + 'sourceCode4.txt', 'r') as src4:
        src = src4.readlines()
        for sentence in src:
            dst.write(sentence.format(name=name,
                                      path_save=path_save,
                                      start=start,
                                      end=end + 1,
                                      factorFuncList=factorFuncList))
