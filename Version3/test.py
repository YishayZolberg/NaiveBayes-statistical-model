from unique_vals import *
from splitDB import divide_file_70_30
unique_vals, dict_corl = class_main()

with open('db.csv') as db:
    reader = csv.reader(db, delimiter=',')
    local_db70, local_db30 = divide_file_70_30(reader)

def calc(dic, userDic):

    buy = 0.0
    not_buy = 0.0
    templen = 0
    yes = 0
    no = 0
    for title, uniq in zip(dic,userDic):
        templen = dic[title][uniq]['yes']+dic[title][uniq]['no']
        yes = dic[title][uniq]['yes']
        no = dic[title][uniq]['no']
        if yes == 0:
            templen += len(dic[title].keys())
            yes += 1
        if no == 0:
            templen += len(dic[title].keys())
            no += 1
        #print(templen, yes, no)
        if buy == 0.0:
            buy = yes / templen
        else:
            buy *= yes / templen

        if not_buy == 0.0:
            not_buy = no / templen
        else:
            not_buy *= no / templen

    # print(f'buy {buy} , \nnot buy {not_buy}')
    buy *= dict_corl['yes'] / sum(dict_corl.values())
    not_buy *= dict_corl['no'] / sum(dict_corl.values())
    # print(f'buy {buy} , \nnot buy {not_buy}')
    return 1 if buy > not_buy else 0

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
    buy_comp_final = []
    list_of_ans = []
    for row in local_db30:
        list_of_ans.append(calc(unique_vals,row[:-1]))
        buy_comp.append(row[-1])
    print(buy_comp)
    print(list_of_ans)

    for i in range(len(buy_comp)):

        if buy_comp[i] == 'yes':
            buy_comp_final.append(1)
        else:
            buy_comp_final.append(0)
    print(buy_comp_final)
    return accuracy(buy_comp_final,list_of_ans)

a = [1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1]
b = [0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0]
print(accuracy(a,b))