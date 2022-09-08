import csv

titles = []
local_db = []

with open('agaricus-lepiota_update.csv') as db:
    reader = csv.reader(db, delimiter=',')
    for row in reader:
        local_db.append(row)
titles = tuple(local_db.pop(0))
unique_values = {}
for i in range(len(local_db)):
    unique_values[i] = local_dby[i][3]
print(set(unique_values.values()))


#for i in range(len(local_db)):
 #   for values in titles:
  #      unique_values[values] = set(unique_values[j][0] for j in range(len(local_db)))
    #if local_db[i][-1] == 'yes':
     #   yes += 1
    #elif local_db[i][-1] == 'no':
     #   no += 1

