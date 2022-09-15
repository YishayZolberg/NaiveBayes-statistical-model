import csv
#the unique values and the number of yes and no cases for each unique value
wnted_unique_vals = {'age': {'middle_age': {'yes': 4, 'no': 0}, 'senior': {'yes': 3, 'no': 2}, 'youth': {'yes': 2, 'no': 3}},
'income': {'high': {'yes': 2, 'no': 2}, 'medium':{'yes': 4, 'no': 2}, 'low':{'yes': 3, 'no': 1}},
'student': {'yes': {'yes': 6, 'no':1 }, 'no': {'yes': 3, 'no': 4}},
'credit_rating': {'excellent': {'yes': 3, 'no':3 }, 'fair': {'yes': 6, 'no': 2}}}

unique_vals= {'age': {'middle_age': {'yes': 0, 'no': 0}, 'senior': {'yes': 0, 'no': 0}, 'youth': {'yes': 0, 'no': 0}},
'income': {'high': {'yes': 0, 'no': 0}, 'medium':{'yes': 0, 'no': 0}, 'low':{'yes': 0, 'no': 0}},
'student': {'yes': {'yes': 0, 'no':0 }, 'no': {'yes': 0, 'no': 0}},
'credit_rating': {'excellent': {'yes': 0, 'no':0 }, 'fair': {'yes': 0, 'no': 0}}}
#the number of yes and no values in Buy_Computer
#choice_dict= {'yes': 9, 'no': 5 }
dict_corl={'no': 0, 'yes': 0}




def csv_data():
    local_db = []
# TO DO : make a check to verify we dont enter empty lines to the local db
    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader: #make a data base of arrays
            local_db.append(row)

    return local_db


def count_corolation(unique_vals, dict_corl, local_db, choice_title, titles):
    #unique_vals = count_set_up(unique_vals, dict_corl, choice_title)
    list = []
    indx = 0
    len1 = len(local_db[0]) - 1
    key_num = ''

    for y_s in dict_corl.keys():
        dict_corl[y_s] = 0
        list.append(y_s)

    indx= titles.index(choice_title)
    del titles[indx]

    #for num, row in len(local_db):
    for number in range(len(local_db[0])):
        for num2, row2 in enumerate(local_db):
            if number <= len(titles)-1 and unique_vals[titles[number]].get(row2[number], None) != None:
                if row2[len1] == list[0]: #if is no
                    unique_vals[titles[number]][row2[number]][list[0]] += 1
                elif row2[len1] == list[1]: #if is yes
                    unique_vals[titles[number]][row2[number]][list[1]] += 1
            elif row2[number] == list[0]:
                dict_corl[list[0]] += 1
            elif row2[number] == list[1]:
                dict_corl[list[1]] += 1

    print(unique_vals)
    print(dict_corl)

choice_title='Buy_Computer'
local_db_m=csv_data()
titles = local_db_m.pop(0)
count_corolation(unique_vals,dict_corl,local_db_m,choice_title,titles)
print(len(local_db_m))