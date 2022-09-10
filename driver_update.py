import csv

ldb = []
with open('agaricus-lepiota_update.csv') as db:
    reader = csv.reader(db, delimiter=',')
    for row in reader:
         ldb.append(row)

#print(ldb)
titles = ldb.pop(0)
#print(titles)
data = {}

for i in range(len(ldb[0])):
    for var in range(len(ldb)):
        data[titles[i]] = []
    for j in range(len(ldb)):
        data[titles[i]].append([ldb[j][i], ldb[j][-1]])
    #   data[titles[i]].append((ldb[j][i]))
#print(data)
ans = {}
for i in data:
    for data_seg in data[i]:
        ans[str(data_seg)] = data[i].count(data_seg)

print(ans)
