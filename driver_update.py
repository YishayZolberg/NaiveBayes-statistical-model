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


# gets the unique values, counts them from the local database construct
# and returns a dict with the unique params and their appearance
def uniqvals(ldb, titles):
    data = {}
    for i in range(len(ldb[0])):
        for var in range(len(ldb)):
            data[titles[i]] = []
        for j in range(len(ldb)):
            data[titles[i]].append((ldb[j][i]))
    data = data[titles[-1]]
    uniq = set(data)
    temp = []
    for uniq_value in uniq:
        temp.append(data.count(uniq_value))
    uniq = dict(zip(uniq, temp))
    return uniq


# updates the ans construct to display the probability of the pair
# appearing in the database as a floating point number; returns ans
def calc(ldb, ans, titles):
    uniq = uniqvals(ldb, titles)
    for value in ans:
        for uniq_val in uniq:
            if uniq_val in value.split()[-1]:
                ans[value] = ans[value] / uniq[uniq_val]
    return ans

    # for title in titles:
    #     temp[title] = set(data[title])
    #     #for value in temp[title]:
    #
    # print(temp)


# main func creating variables for ease of use
def main():
    ldb = create_ldb()
    titles = create_titles(ldb)
    data = create_data(ldb, titles)
    ans = create_anskey(data)
    ans = calc(ldb, ans, titles)
    print(ans.keys(), "\nhere are your available options:")

if __name__ == "__main__":
    main()
