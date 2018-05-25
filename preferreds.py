
import csv
from operator import itemgetter

prefFile = open('data/Preferreds.csv')
prefReader = csv.reader(prefFile)
prefData = list(prefReader)
FORMAT = '{:45} {:7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>13} {:>12} {:>12} {:>7} {:>7} {:>9}'

#remove the first three items from the list

for i in range(3):
    del prefData[0]

headerRow = prefData[0]
del prefData[0]

print(FORMAT.format(*headerRow))


for i in range(len(prefData)):
    if prefData[i][12] == '...':
        prefData[i][12] = float(0.00)


newList = sorted(prefData, key=lambda x: float(x[12]), reverse = True)

for row in newList:
    row[0] = row[0][:40]
    print(FORMAT.format(*row))


## Columns/Elements
## (0)name
## (1)symbol
## (2)open
## (3)high
## (4)low
## (5)close
## (6)net chg
## (7)% chg
## (8)volume
## (9)52 wk high
## (10)52 wk low
## (11)div
## (12)yield
## (13)ytd % chg

