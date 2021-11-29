import pandas as pd
import os


class DayFactor:
    def __init__(self, dayFacDict):
        self.daydf = dayFacDict
        return


class Factor:

    def __init__(self, factor_category, id_in_category, dayFactorList=None):
        self.category = factor_category
        self.id = id_in_category
        if dayFactorList is None:
            self.dayFactorList = []
        else:
            self.dayFactorList = dayFactorList
        return

    def addOneDay(self, aDayFactor: DayFactor):
        assert type(aDayFactor) == DayFactor
        self.dayFactorList.append(aDayFactor.daydf)
        return

    def addMultDays(self, dayFactorList):
        assert type(dayFactorList) == list
        if len(dayFactorList) > 0:
            assert type(dayFactorList[0]) == DayFactor
        for dayFactor in dayFactorList:
            self.dayFactorList.append(dayFactor.daydf)
        return

    def addMultDict(self, dictList):
        assert type(dictList) == list
        if len(dictList) > 0:
            assert type(dictList[0]) == dict
        for aDict in dictList:
            self.dayFactorList.append(aDict)
        return

    def getLen(self):
        return len(self.dayFactorList)

    def write_csv(self, datesIdx):
        resDict2csv(self.dayFactorList, datesIdx, self.category, self.id)
        return


resDir = 'D:/tick_factor/tick_{}/'
resPath = 'D:/tick_factor/tick_{}/{}.csv'


def resDict2csv(resDictList, dateData, factor_name, factor_ID):
    tmp = pd.DataFrame(resDictList, index=dateData)
    xdir = resDir.format(factor_name)
    if os.path.exists(xdir):
        pass
    else:
        os.makedirs(xdir)
    tmp.to_csv(resPath.format(factor_name, factor_name + factor_ID))
    return
