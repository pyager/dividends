import csv

prefFile = open('data/Preferreds.csv')
prefReader = csv.reader(prefFile)
prefData = list(prefReader)

#remove the first three items from the list

for i in range(3):
	del prefData[0]

		
for row in prefData:
		print('{:15} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5} {:5}'.format(*row))
    # print(row)


