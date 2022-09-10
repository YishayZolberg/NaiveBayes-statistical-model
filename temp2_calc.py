import csv
def csv_data():
    local_db = []

    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader: #make a data base of arrays
            local_db.append(row)

    return local_db

def make_unique(local_db):
    titles = []
    unique_vals = {}
    temp_list = []

    titles = local_db[0]
    unique_vals = dict.fromkeys(titles, ' ')

    for num, row in enumerate(local_db):
        for number, col in enumerate(row):
            for num2, row2 in enumerate(local_db):
                temp_list.append(local_db[num2][number])
            for i, key in enumerate(unique_vals):
                if i == number:
                    unique_vals[key] = set(temp_list)
            temp_list.clear()
    #print(unique_vals)
    return unique_vals


def choice_question(local_db, choice):
    #here we would have the user input the choice of classification column:
    # true for first and false for last
    ques_col = []
    ques_col_set= []
    #choice = False


    for num, row in enumerate(local_db):
        for number, col in enumerate(row):
            for num2, row2 in enumerate(local_db):
                if choice == True and number == 0:
                    ques_col.append(local_db[num2][number])
                    ques_col_set = set(ques_col)

                elif choice == False and number == (len(row)-1) :
                    ques_col.append(local_db[num2][number])
                    ques_col_set = set(ques_col)

    dict_corl = dict.fromkeys(ques_col_set, 0)
    return dict_corl


def count_set_up(unique_vals, dict_corl):
    temp = {}

    for key, value in unique_vals.items():
        temp = dict.fromkeys(value, ' ')
        for value2 in value:
            temp[value2] = dict_corl
        unique_vals[key]=temp

    #return unique_vals

def count_corolation(unique_vals, dict_corl, local_db):
    count_set_up(unique_vals, dict_corl)
    list = []
    indx = 0
    len1 = len(local_db[0])-1
    len2 = len(local_db[0]) - 2
    for y_s in dict_corl.keys():
        list.append(y_s)

    for num, row in enumerate(local_db):
        for number, col in enumerate(row):
            for key in unique_vals.keys():
                if number == len1:

                    if unique_vals[key].get(col, None) != None and row[len1] == list[0]: #if is no
                        unique_vals[key][col][list[0]] =+ 1
                    elif unique_vals[key].get(col, None) != None and row[len1] == list[1]: #if is yes
                        unique_vals[key][col][list[1]] =+ 1

    print(unique_vals)




global_db = []
unique= {}
dict_corl_m = {}
global_db = csv_data()
unique = make_unique(global_db)
dict_corl_m = choice_question(global_db, False)

count_corolation(unique, dict_corl_m, global_db)
