# 第四个版本 不进行sliceTime， 读一天算一天，为了防止内存爆炸，在读的队列里规定最大能读取的内容
import itertools
import time
from study_orderImbalance.orderImbalance3to6_new import (calcVolDiff, orderImbalance_3,
                                                         orderImbalance_4, orderImbalance_5, orderImbalance_6)
from Factor import DayFactor, Factor
from readTickDataParallel2 import readFunc, tdatelist, timeFlage
from multiprocessing import Process, Manager
from collections import deque
import numpy as np


#
def concatDict(dictDeque):
    if dictDeque:
        res = dictDeque.popleft()
    else:
        return {}
    while dictDeque:
        a_dict = dictDeque.popleft()
        for key in a_dict:
            if key in res.key:
                res[key] = np.concatenate((res[key], a_dict[key]), axis=0)
            else:
                res[key] = a_dict[key]
    return res


def commonCalcFunc(dataDictList):
    res = {}
    dataDict = concatDict(dataDictList)
    for inst in dataDict:
        #
        res[inst] = calcVolDiff(dataDict[inst])
    return res


#
def factorCalcFunc(dataDictList, aFunc):
    res = {}
    for inst in dataDictList:
        res[inst] = aFunc(dataDictList[inst])
    return DayFactor(res)


def readFunc_iter(dateList, q, window):
    tmpData = deque([], maxlen=window)
    for i in range(window):
        tmpData.append(readFunc(dateList[i]))
    q.put(tmpData)
    for i in range(window, len(dateList)):
        tmpData.popleft()
        tmpData.append(readFunc(dateList[i]))
        q.put(tmpData)
    q.put(None)
    return

win = 1
funcSet = [orderImbalance_3, orderImbalance_4, orderImbalance_5, orderImbalance_6]
name = 'orderImbalance_test4_'
Factor3 = Factor(name, '3')
Factor4 = Factor(name, '4')
Factor5 = Factor(name, '5')
Factor6 = Factor(name, '6')
factorSet = [Factor3, Factor4, Factor5, Factor6]
tdatelist1 = tdatelist[:3]
nlen = len(tdatelist1)
readDate = list(itertools.product(tdatelist1, timeFlage))


def handle_iter(src_q):
    while True:
        data = src_q.get()
        if data is None:
            dateData = list(itertools.product(tdatelist1, timeFlage))
            for factor in factorSet:
                print(factor.dayFactorList)
                factor.write_csv(dateData)
            break
        else:
            tmpRes = commonCalcFunc(data)
            for funcID, func in enumerate(funcSet):
                res = factorCalcFunc(tmpRes, func)
                factorSet[funcID].addOneDay(res)
                print(factorSet[funcID].dayFactorList)
        print('one day complete!')
    return


if __name__ == '__main__':
    start = time.perf_counter()
    # use single thread to read
    with Manager() as m:
        dfQueue = m.Queue(maxsize=10)
        readProcess = Process(target=readFunc_iter, args=(readDate, dfQueue, win))
        readProcess.start()
        handleProcess = Process(target=handle_iter, args=(dfQueue,))
        handleProcess.start()
        handleProcess.join()
        readProcess.join()
    end = time.perf_counter()
    print("final is in : %s Seconds " % (end - start))
