#TODO:
# take the the data file and make it useable
# make array of unique values
# make comarison for values and counts them as yes or no
# puts results in array, calculation of fractions into result.

import csv

#opens the the data file and makes it useable
def csv_data():
    local_db = []
    titles = []
    unique_values = {}
    row_length = 0
    col_length = 0

    title = False
    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        print(reader)
        for i, row in enumerate(reader):
            #make a data base of arrays
            local_db.append(row)



            if i == 1:
                titles = local_db.pop(0)
                unique_values.setdefault(titles[i], {})[' '] = ' '
            #print("this is titles:", titles)

            #if title == True:
            for j in range(len(row)):
                unique_values.setdefault(titles[j], {})[' '] = ' '
            # print("this is unique values",unique_values)
            #title = False

            # if title == False:
            #     for col in range(len(row)):
            #         # if col not in unique_values.keys[col]:
            #         if row[col] not in unique_values[titles[col]]:
            #             unique_values[titles[col]] = row[col]
            #             pass
            #     print("this is unique values2",unique_values)
            row_length += 1
            #     test_dict.setdefault(1, {})[4] = 7

            # if title == False: # and col_length < len(row):
            #     for col in row:
            #         if col not in unique_values[titles[col_length]]:
            #             unique_values[titles[col_length]] = col
            #         col_length += 1



    #make_unique(local_db, titles, unique_values)


#make array of unique values
def make_unique(local_db, titles, unique_values):
    col_length = 0
    for row in local_db:
        for col in row:
            if col not in unique_values.values[col_length]:
                print(unique_values[titles[col_length]])
                unique_values[titles[col_length]] = col

            col_length += 1
        col_length = 0
    print("this is unique values", unique_values)

#make comarison for values and counts them as green or red
def insert_stat():
    pass
#puts results in array, calculation of fractions into result.
def calc_result():
    pass

csv_data()
