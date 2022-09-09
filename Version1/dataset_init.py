import csv
file = 'dataset.csv'
def Iitialize(file):
	"""
	Can run only with CSV import !!!Important!!!
	This function gets a dataset and convert it to list of row lists
	Also pop the first row of titles to Set
	:param file: db csv file
	:return: 2 values - first db second titels of db
	"""
	local_db = []
	with open(file, encoding='utf-8') as File:
		Reader = csv.reader(File, delimiter=',')

		for row in Reader:
			local_db.append(row)
	titles = tuple(local_db.pop(0))
	return local_db ,titles

dataset,titels = Iitialize(file)
print(dataset)
print(titels)