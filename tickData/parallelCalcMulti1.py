# 第四个版本 不进行sliceTime， 读一天算一天，为了防止内存爆炸，在读的队列里规定最大能读取的内容
import itertools
import time
from study_smartVol.smartVol27 import (calcVolQuantile, smartVol27)
from Factor import DayFactor, Factor
from readTickDataParallel2 import readFunc, tdatelist, timeFlage, handleTickDataComplete
from multiprocessing import Process, Manager
from collections import deque, defaultdict
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
            if key in res.keys():
                res[key] = np.concatenate((res[key], a_dict[key]), axis=0)
            else:
                res[key] = a_dict[key]
    return res


#
def reverseListOfDict(dictList):
    res = defaultdict(list)
    for idx, a_dict in enumerate(dictList):
        for key in a_dict:
            res[key].append(idx)
    return res


def concatDict1(dictList):
    res = {}
    idxDict = reverseListOfDict(dictList)
    for key in idxDict:
        res[key] = np.concatenate([dictList[i][key] for i in idxDict[key]], axis=0)
    return res


def commonCalcFunc(dataDict):
    res = {}
    for inst in dataDict:
        #
        res[inst] = calcVolQuantile(dataDict[inst])
    return res


#
def factorCalcFunc(dataDictList, aFunc):
    res = {}
    for inst in dataDictList:
        res[inst] = aFunc(dataDictList[inst])
    return DayFactor(res)


def readFunc_iter(dateList, des_q):
    for date in dateList:
        des_q.put(readFunc(date))
        print(date)
    des_q.put(None)
    return


def handle_iter(src_q, des_q):
    while True:
        data = src_q.get()
        if data is None:
            des_q.put(None)
            break
        else:
            dict_of_arr2d = {inst: handleTickDataComplete(df) for inst, df in data.items()}
            des_q.put(dict_of_arr2d)
    return


def concat_iter(src_q, des_q, window):
    tmpData = deque([], maxlen=window)
    while True:
        dict_of_arr = src_q.get()
        if dict_of_arr is None:
            des_q.put(None)
            break
        tmpData.append(dict_of_arr)
        if len(tmpData) == window:
            des_q.put(concatDict1(list(tmpData)))
    return


win = 3

funcSet = [smartVol27]

name = 'smartVol_win=3_'

Factor27 = Factor(name, '27')


factorSet = [Factor27]
tdatelist1 = tdatelist
nlen = len(tdatelist1)
readDate = list(itertools.product(tdatelist1, timeFlage))


def calc_iter(src_q):
    while True:
        data = src_q.get()
        if data is None:
            dateData = list(itertools.product(tdatelist1, timeFlage))[(win - 1):]
            for factor in factorSet:
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
        arr2dQueue = m.Queue(maxsize=10)
        multiArrQueue = m.Queue(maxsize=10)
        readProcess = Process(target=readFunc_iter, args=(readDate, dfQueue))
        readProcess.start()
        handleProcess = Process(target=handle_iter, args=(dfQueue, arr2dQueue))
        handleProcess.start()
        concatProcess = Process(target=concat_iter, args=(arr2dQueue, multiArrQueue, win))
        concatProcess.start()
        calcProcess = Process(target=calc_iter, args=(multiArrQueue,))
        calcProcess.start()
        calcProcess.join()
        concatProcess.join()
        handleProcess.join()
        readProcess.join()
    end = time.perf_counter()
    print("final is in : %s Seconds " % (end - start))
