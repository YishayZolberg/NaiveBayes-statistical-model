import csv
from splitDB import divide_file_70_30
#the unique values and the number of yes and no cases for each unique value
unique_vals = {'age': {'middle_age': {'yes': 4, 'no': 0}, 'senior': {'yes': 3, 'no': 2}, 'youth': {'yes': 2, 'no': 3}},
'income': {'high': {'yes': 2, 'no': 2}, 'medium':{'yes': 4, 'no': 2}, 'low':{'yes': 3, 'no': 1}},
'student': {'yes': {'yes': 6, 'no':1 }, 'no': {'yes': 3, 'no': 4}},
'credit_rating': {'excellent': {'yes': 3, 'no':3 }, 'fair': {'yes': 6, 'no': 2}}}

#the number of yes and no values in Buy_Computer
choice_dict= {'yes': 9, 'no': 5 }

def yishay_calc(dic, userDic):
    buy = 0.0
    not_buy = 0.0
    templen = 0
    for title, uniq in zip(dic,userDic):
        templen = dic[title][uniq]['yes']+dic[title][uniq]['no']
        if buy == 0.0:
            buy = dic[title][uniq]['yes'] / templen
            not_buy = dic[title][uniq]['no'] / templen
        else:
            buy *= dic[title][uniq]['yes']/templen
            not_buy *= dic[title][uniq]['no']/templen
    #print(buy)
    #print(not_buy)
    return 1 if buy > not_buy else 0

a = ['senior','high','no','fair']
print(yishay_calc(unique_vals,a))


with open('db.csv') as db:
    reader = csv.reader(db, delimiter=',')
    local_db70, local_db30 = divide_file_70_30(reader)

# For test
#print(f'localdb30: {local_db30}')


def accuracy(y_true,y_pred):
    count = 0
    correct = 0
    for i in range(len(y_true)):
        count += 1
        if y_true[i] == y_pred[i]:
            correct += 1
    acc = correct / count
    return round(acc,4)

def check_probability(local_db30):
    buy_comp = []
    buy_comp2 = []
    list_of_ans = []
    for row in local_db30:
        list_of_ans.append(yishay_calc(unique_vals,row[:-1]))
        buy_comp.append(row[-1])

    for i in range(len(buy_comp)):

        if buy_comp[i] == 'yes':
            buy_comp2.append(1)
        else:
            buy_comp2.append(0)
    return accuracy(buy_comp2,list_of_ans)


local_dbpop = local_db70.pop(0)
print(local_db70)

print(check_probability(local_db70))








