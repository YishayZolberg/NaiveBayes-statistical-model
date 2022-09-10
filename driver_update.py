import csv


# conversion of csv file into a database construct
def create_ldb():
    ldb = []
    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader:
            ldb.append(row)
    return ldb


# creating titles from the first line in the csv file, interaction is through the ldb object
def create_titles(ldb):
    titles = ldb.pop(0)
    return titles


# creating the data construct to get only the colum value and the last value in the line(the denominator)
def create_data(ldb, titles):
    data = {}
    for i in range(len(ldb[0])):
        for var in range(len(ldb)):
            data[titles[i]] = []
        for j in range(len(ldb)):
            data[titles[i]].append([ldb[j][i], ldb[j][-1]])
        #   data[titles[i]].append((ldb[j][i])) ; to get only the values in order of the list without the denominator.
    return data


# creating the answer key, containing all possible combination between the columns and the the last colum
# and how many times these combination apper in the csv file
def create_anskey(data):
    ans = {}
    for i in data:
        for data_seg in data[i]:
            ans[str(data_seg)] = data[i].count(data_seg)
    return ans

# main func creating variables for ease of use
def main():
    ldb = create_ldb()
    titles = create_titles(ldb)
    data = create_data(ldb, titles)
    ans = create_anskey(data)
    print(data)
    print(ans)


if __name__ == "__main__":
    main()
