import csv

local_db = []
titles = []
unique_values = {}
length = 0

with open('db.csv') as db:
    reader = csv.reader(db, delimiter=',')
    for row in reader:
        local_db.append(row)

titles = tuple(local_db.pop(0))

for i in range(len(local_db)):
    unique_values[i] = local_db[i]
length = len(local_db)

def calculator(local_db):
    uniqe_type=[]
    current_col = 2
    for x in local_db:
        if x[current_col] not in uniqe_type:
            uniqe_type.append(x[current_col])
    print(uniqe_type)
calculator(local_db)