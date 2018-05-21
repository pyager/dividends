import csv

prefFile = open('data/Preferreds.csv')
prefReader = csv.reader(prefFile)
prefData = list(prefReader)

#remove the first three items from the list

for i in range(3):
	del prefData[0]

		
for i in range(len(prefData)):
    temp = prefData[i][0]
    temp = temp[:40]
    prefData[i][0] = temp
##    print(prefData[i][0])

for row in prefData:
    print('{:45} {:7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>13} {:>12} {:>12} {:>7} {:>7} {:>9}'.format(*row))


