import pandas as pd
import os
import itertools
from collections import defaultdict


PATH = 'D:/tick/tick/{}_{}'
tdatelist = list(pd.read_csv('D:/tick/tick/date.csv')['0'])
SYMBOLS =  ['AG', 'AL', 'AU', 'BU', 'C', 'CF', 'CU', 'EB', 'EG', 'FG', 'FU',
            'HC', 'I', 'J', 'JM', 'L', 'M', 'MA', 'NI', 'OI', 'P', 'PF', 'PP',
            'RB', 'RM', 'RU', 'SA', 'SC', 'SP', 'TA', 'V', 'Y', 'ZC', 'ZN']
timeFlage = [1, 2, 3]


# format the res
idx = defaultdict(list)
for tdate, timeflage in itertools.product(tdatelist, timeFlage):
    directory = PATH.format(tdate, timeflage)

    for root, dirs, files in os.walk(directory):
        for file in files:
            name, fileType = file.split('.')
            idx[name].append('{}_{}'.format(tdate, timeflage))

for key in idx:
    pd.DataFrame(idx[key]).to_csv('D:/tick/{}.csv'.format(key), index=False)
