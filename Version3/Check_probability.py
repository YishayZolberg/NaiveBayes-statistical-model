from splitDB import divide_file_70_30
from calculation import yishay_calc
from unique_vals import class_main
import csv


unique_vals, dict_corl = class_main()

with open('db.csv') as db:
    reader = csv.reader(db, delimiter=',')
    local_db70, local_db30 = divide_file_70_30(reader)


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
        list_of_ans.append(yishay_calc(unique_vals,row[:-1]))
        buy_comp.append(row[-1])

    for i in range(len(buy_comp)):

        if buy_comp[i] == 'yes':
            buy_comp_final.append(1)
        else:
            buy_comp_final.append(0)
    return accuracy(buy_comp_final,list_of_ans)


#print(check_probability(local_db30))


