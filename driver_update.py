import csv


class Ldb:
    def __init__(self):
        self.ldb = self.create_ldb()
        self.titles = self.create_titles()
        self.data = self.create_data()
        self.ans = self.create_anskey()
        self.tempdata = []
        self.tempdata_copy = []
        self.uniq = self.unique_vals()
        self.denominator_val = self.create_denominator_val()

    # conversion of csv file into a database construct
    def create_ldb(self):
        self.ldb = []
        with open('db.csv') as db:
            reader = csv.reader(db, delimiter=',')
            for row in reader:
                self.ldb.append(row)
        return self.ldb

    # creating titles from the first line in the csv file, interaction is through the ldb object
    def create_titles(self):
        self.titles = self.ldb.pop(0)
        return self.titles

    # creating the data construct to get only the colum value and the last value in the line(the denominator)

    def create_data(self):
        self.data = {}
        for i in range(len(self.ldb[0])):
            for var in range(len(self.ldb)):
                self.data[self.titles[i]] = []
            for j in range(len(self.ldb)):
                self.data[self.titles[i]].append([self.ldb[j][i], self.ldb[j][-1]])
        return self.data

    # creating the answer key, containing all possible combination between the columns and the the last colum
    # and how many times these combination apper in the csv file
    def create_anskey(self):
        self.ans = {}
        for i in self.data:
            for data_seg in self.data[i]:
                self.ans[str(data_seg)] = self.data[i].count(data_seg)
        return self.ans

    # gets the unique values, counts them from the local database construct
    # and returns a dict with the unique params and their appearance
    def unique_vals(self):
        self.tempdata = {}
        for i in range(len(self.ldb[0])):
            for var in range(len(self.ldb)):
                self.tempdata[self.titles[i]] = []
            for j in range(len(self.ldb)):
                self.tempdata[self.titles[i]].append((self.ldb[j][i]))
        self.tempdata_copy = self.tempdata
        self.tempdata = self.tempdata[self.titles[-1]]
        self.uniq = set(self.tempdata)
        temp = []
        for uniq_value in self.uniq:
            temp.append(self.tempdata.count(uniq_value))
        self.uniq = dict(zip(self.uniq, temp))
        print(self.uniq)
        return self.calc()

    # creates the denominator value list, with the unique values in the denominator collum 
    # and their appearance in a floating point number out of the length of objects in the tabel

    def create_denominator_val(self):
        self.denominator_val = []
        for value in self.tempdata_copy:
            self.tempdata_copy[value] = set(self.tempdata_copy[value])
        for uniq_value in self.uniq:
            if self.tempdata.count(uniq_value) == 0:
                self.denominator_val.append((self.tempdata.count(uniq_value) + 1)
                                            / len(self.tempdata) + len(set(self.tempdata)))
        self.denominator_val = dict(zip(self.uniq, self.denominator_val))
        return self.denominator_val

    # updates the ans construct to display the probability of the pair
    # appearing in the database as a floating point number; returns ans
    def calc(self):
        for value in self.ans:
            for uniq_val in self.uniq:
                if uniq_val in value.split()[-1]:
                    if self.ans[value] == 0 or self.uniq[uniq_val] == 0:
                        self.ans[value] = (self.ans[value] + 1) / (self.uniq[uniq_val] + len(self.uniq))
                    else:
                        self.ans[value] = (self.ans[value]) / (self.uniq[uniq_val])
        return self.ans

    # def __str__(self):
    #     print(self.ans.keys(), "\nhere are your available options:")
    #     print(self.ans)


if __name__ == "__main__":
    test = Ldb()
    print(test)
