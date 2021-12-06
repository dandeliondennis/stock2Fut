# 第四个版本 不进行sliceTime， 读一天算一天，为了防止内存爆炸，在读的队列里规定最大能读取的内容
import itertools
import time
from study_smartVol.smartVol12_para import (calcVolQuantile, smartVol12_0, smartVol12_1, smartVol12_2,
                                            smartVol12_3, smartVol12_4, smartVol12_test)

from Factor import DayFactor, Factor
from readTickDataParallel2 import readFunc, tdatelist, timeFlage, handleTickDataComplete
from multiprocessing import Process, Manager


#
def commonCalcFunc(dataDict):
    res = {}
    for inst in dataDict:
        #
        res[inst] = calcVolQuantile(handleTickDataComplete(dataDict[inst]))
    return res


#
def factorCalcFunc(dataDictList, aFunc):
    res = {}
    for inst in dataDictList:
        res[inst] = aFunc(dataDictList[inst])
    return DayFactor(res)


def readFunc_iter(dateList, q):
    for date in dateList:
        q.put(readFunc(date))
        print(date)
    q.put(None)
    return


funcSet = [smartVol12_0, smartVol12_1, smartVol12_2,
           smartVol12_3, smartVol12_4, smartVol12_test]
name = 'smartVol_'
Factor12_0 = Factor(name, '12_0')
Factor12_1 = Factor(name, '12_1')
Factor12_2 = Factor(name, '12_2')
Factor12_3 = Factor(name, '12_3')
Factor12_4 = Factor(name, '12_4')
Factor12_test = Factor(name, '12_test')

factorSet = [Factor12_0, Factor12_1, Factor12_2, Factor12_3, Factor12_4, Factor12_test]
tdatelist1 = tdatelist[:]
nlen = len(tdatelist1)
readDate = itertools.product(tdatelist1, timeFlage)


def handle_iter(src_q):
    while True:
        data = src_q.get()
        if data is None:
            dateData = list(itertools.product(tdatelist1, timeFlage))
            for factor in factorSet:
                # print(factor.dayFactorList)
                factor.write_csv(dateData)
            break
        else:
            tmpRes = commonCalcFunc(data)
            for funcID, func in enumerate(funcSet):
                res = factorCalcFunc(tmpRes, func)
                factorSet[funcID].addOneDay(res)
                # print(factorSet[funcID].dayFactorList)
    return


if __name__ == '__main__':
    start = time.perf_counter()
    # use single thread to read
    with Manager() as m:
        dfQueue = m.Queue(maxsize=10)
        readProcess = Process(target=readFunc_iter, args=(readDate, dfQueue))
        readProcess.start()
        handleProcess = Process(target=handle_iter, args=(dfQueue,))
        handleProcess.start()
        handleProcess.join()
        readProcess.join()
    end = time.perf_counter()
    print("final is in : %s Seconds " % (end - start))
