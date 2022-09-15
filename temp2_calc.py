import csv
def csv_data():
    local_db = []
# TO DO : make a check to verify we dont enter empty lines to the local db
    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader: #make a data base of arrays
            local_db.append(row)

    return local_db

def make_unique(local_db):
    titles = []
    unique_vals = {}
    temp_list = []

    titles = local_db.pop(0)
    unique_vals = dict.fromkeys(titles, ' ')

    for num, row in enumerate(local_db):
        for number, col in enumerate(row):
            for num2, row2 in enumerate(local_db):
                if num2 < len(local_db) and number < len(local_db[0])-1:
                    temp_list.append(local_db[num2][number])
            for i, key in enumerate(unique_vals):
                if i == number:
                    unique_vals[key] = set(temp_list)
            temp_list.clear()
    print(unique_vals)
    return unique_vals, titles


def choice_question(local_db, choice, titles, unique_vals):
    #here we would have the user input the choice of classification column:
    # true for first and false for last
    ques_col = []
    ques_col_set = []
    choice_title = ' '

    for num, row in enumerate(local_db):
        for number, col in enumerate(row):
            for num2, row2 in enumerate(local_db):
                if choice == True and number == 0:
                    ques_col.append(local_db[num2][number])
                    ques_col_set = set(ques_col)
                    choice_title = titles[0]


                elif choice == False and number == (len(row)-1) :
                    ques_col.append(local_db[num2][number])
                    ques_col_set = set(ques_col)
                    choice_title = titles[-1]

    del unique_vals[choice_title]
    dict_corl = dict.fromkeys(ques_col_set, 0)
    return dict_corl, choice_title


def count_set_up(unique_vals, dict_corl, choice_title):
    temp = {}
    for key, value in unique_vals.items():
        temp = dict.fromkeys(value, ' ')
        for value2 in value:
            temp[value2] = dict_corl
        unique_vals[key]=temp
    return unique_vals


def count_corolation(unique_vals, dict_corl, local_db, choice_title, titles):
    unique_vals = count_set_up(unique_vals, dict_corl, choice_title)
    list = []
    indx = 0
    len1 = len(local_db[0]) - 1
    #len2 = len(local_db[0]) - 2
    for y_s in dict_corl.keys():
        dict_corl[y_s] = 0
        list.append(y_s)

    indx= titles.index(choice_title)
    del titles[indx]
    for num, row in enumerate(local_db):
        for number, col in enumerate(row):
            for num2, row2 in enumerate(local_db):
                # if str([titles[number]]) != str(choice_title):
                # print('title[number]',titles[number],choice_title)
                if unique_vals[titles[number]].get(col, None) != None and row[len1] == list[0]: #if is no
                    unique_vals[titles[number]][col][list[0]] =+ 1
                elif unique_vals[titles[number]].get(col, None) != None and row[len1] == list[1]: #if is yes
                    unique_vals[titles[number]][col][list[1]] =+ 1
            # for key in unique_vals.keys():
            #     if unique_vals[key].get(col, None) != None and row[len1] == list[0]: #if is no
            #         unique_vals[key][col][list[0]] =+ 1
            #     elif unique_vals[key].get(col, None) != None and row[len1] == list[1]: #if is yes
            #         unique_vals[key][col][list[1]] =+ 1
    print(type(choice_title), type(titles[0]))
    print(unique_vals)
    print(dict_corl, list)




global_db = []
unique= {}
dict_corl_m = {}
global_db = csv_data()
unique, titles_m = make_unique(global_db)
print(titles_m)
dict_corl_m, choice_title = choice_question(global_db, False, titles_m, unique)

#count_corolation(unique, dict_corl_m, global_db, choice_title, titles_m)