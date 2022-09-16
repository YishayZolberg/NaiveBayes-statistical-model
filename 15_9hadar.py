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

#this function inserts the third layes of the data model: the unique options of the question column
def count_set_up(unique_vals, dict_corl):
    temp = {}
    for key, value in unique_vals.items():
        temp = dict.fromkeys(value, ' ')

        for value2 in value:
            temp[value2] = dict_corl
        unique_vals[key]=temp

    return unique_vals

choice_title='Buy_Computer'
local_db_m=csv_data()
count_set_up(unique_vals,dict_corl)
