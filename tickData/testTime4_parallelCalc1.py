# 第四个版本 不进行sliceTime， 读一天算一天，为了防止内存爆炸，在读的队列里规定最大能读取的内容
import itertools
import time
from multiprocessing import Process, Manager

from Factor import DayFactor, Factor
from readTickDataParallel2 import readFunc, tdatelist, timeFlage, handleTickDataComplete
from study_smallVolNoise.smallVolNoise0to1 import (calcVolQuantile, smallVolNoise0_0, smallVolNoise0_1,
                                                   smallVolNoise0_2,
                                                   smallVolNoise0_3, smallVolNoise0_4, smallVolNoise0_5,
                                                   smallVolNoise0_6, smallVolNoise0_7, smallVolNoise0_8,
                                                   smallVolNoise0_9, smallVolNoise0_10, smallVolNoise0_11,
                                                   smallVolNoise0_12)


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


funcSet = [smallVolNoise0_0, smallVolNoise0_1, smallVolNoise0_2,
           smallVolNoise0_3, smallVolNoise0_4, smallVolNoise0_5,
           smallVolNoise0_6, smallVolNoise0_7, smallVolNoise0_8,
           smallVolNoise0_9, smallVolNoise0_10, smallVolNoise0_11,
           smallVolNoise0_12]

name = 'smallVolNoise_'
Factor0_0 = Factor(name, '0_0')
Factor0_1 = Factor(name, '0_1')
Factor0_2 = Factor(name, '0_2')
Factor0_3 = Factor(name, '0_3')
Factor0_4 = Factor(name, '0_4')
Factor0_5 = Factor(name, '0_5')
Factor0_6 = Factor(name, '0_6')
Factor0_7 = Factor(name, '0_7')
Factor0_8 = Factor(name, '0_8')
Factor0_9 = Factor(name, '0_9')
Factor0_10 = Factor(name, '0_10')
Factor0_11 = Factor(name, '0_11')
Factor0_12 = Factor(name, '0_12')

factorSet = [Factor0_0, Factor0_1, Factor0_2, Factor0_3,
             Factor0_4, Factor0_5, Factor0_6, Factor0_7,
             Factor0_8, Factor0_9, Factor0_10, Factor0_11,
             Factor0_12]
tdatelist1 = tdatelist
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
