import pandas as pd
import os


SYMBOLS = ['AG', 'AL', 'AU', 'BU', 'C', 'CF', 'CU', 'EB', 'EG', 'FG', 'FU',
           'HC', 'I', 'J', 'JM', 'L', 'M', 'MA', 'NI', 'OI', 'P', 'PF', 'PP',
           'RB', 'RM', 'RU', 'SA', 'SC', 'SP', 'TA', 'V', 'Y', 'ZC', 'ZN']


idx = {}
for inst in SYMBOLS:
    idx[inst] = pd.read_csv('D:/tick/{}.csv'.format(inst))['0']

resDir = 'D:/tick_factor/tick_{}/'
resPath = 'D:/tick_factor/tick_{}/{}.csv'


def resDict2csv(resDictList, dateData, factor_name, factor_ID):
    tmp = pd.DataFrame(resDictList, index=dateData)
    xdir = resDir.format(factor_name)
    if os.path.exists(xdir):
        pass
    else:
        os.makedirs(xdir)
    tmp.to_csv(resPath.format(factor_name, factor_name+factor_ID))
    return


def resDict2csv1(resDictList, dateData, factor_name):
    tmp = pd.DataFrame(resDictList, index=dateData)
    xdir = resDir.format(factor_name)
    if os.path.exists(xdir):
        pass
    else:
        os.makedirs(xdir)
    tmp.to_csv(resPath.format(factor_name, factor_name))
    return


def multiResDict2csv(resDict, dateData, start, factor_name):
    for inst in resDict:
        idx = ['{}_{}'.format(i, j) for i, j in dateData[inst][start:]]
        tmp = pd.DataFrame(resDict[inst], index=idx, columns=[inst])
        dir = resDir.format(factor_name)
        if os.path.exists(dir):
            pass
        else:
            os.makedirs(dir)
        tmp.to_csv(resPath.format(factor_name, inst))
    return


def multiResDict2csv1(resDictList, dateData, factor_name):
    tmp = pd.DataFrame(resDictList, index=dateData)
    dir = resDir.format(factor_name)
    if os.path.exists(dir):
        pass
    else:
        os.makedirs(dir)
    tmp.to_csv(resPath.format(factor_name, factor_name))
    return