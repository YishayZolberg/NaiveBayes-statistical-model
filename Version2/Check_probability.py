import csv
from splitDB import divide_file_70_30

#the unique values and the number of yes and no cases for each unique value
unique_vals = {'age': {'middle_age': {'yes': 4, 'no': 0}, 'senior': {'yes': 3, 'no': 2}, 'youth': {'yes': 2, 'no': 3}},
'income': {'high': {'yes': 2, 'no': 2}, 'medium':{'yes': 4, 'no': 2}, 'low':{'yes': 3, 'no': 1}},
'student': {'yes': {'yes': 6, 'no':1 }, 'no': {'yes': 3, 'no': 4}},
'credit_rating': {'excellent': {'yes': 3, 'no':3 }, 'fair': {'yes': 6, 'no': 2}}}

#the number of yes and no values in Buy_Computer
choice_dict= {'yes': 9, 'no': 5 }

# unique_titles = []
# unique_option = []
# for key,value in unique_vals.items():
#     unique_titles.append(key)
#     print(unique_titles)
#     for val in value:
#         if val not in unique_option:
#             unique_option.append(val)
# print(unique_option)





with open('db.csv') as db:
    reader = csv.reader(db, delimiter=',')
    local_db70, local_db30 = divide_file_70_30(reader)

# For test
#print(f'localdb30: {local_db30}')


def check_probability(local_db30):

    for row in local_db30:
        print(row)

check_probability(local_db30)







