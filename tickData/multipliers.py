import pandas as pd


CHANGETDATE = pd.to_datetime('20180326')
ZZSYMBOLS = ['CF', 'FG', 'MA', 'OI', 'PF', 'RM', 'SA', 'TA', 'ZC']
multipliers = pd.read_csv('D:/multipliers.csv')
multipliers['instrument'] = multipliers['instrument'].apply(lambda string: string.upper())
multipliers.set_index(['instrument'], inplace=True)
multipliers1 = multipliers.copy(deep=True)
multipliers1.loc[ZZSYMBOLS, :] = 1
