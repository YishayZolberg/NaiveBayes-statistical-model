import csv
TITLES = []
LOCAL_DB=[]

with open('db.csv') as db:
    reader = csv.reader(db, delimiter=',')
    for row in reader:
        LOCAL_DB.append(row)
TITLES=LOCAL_DB[0].pop()
print(LOCAL_DB)
print(TITLES)


