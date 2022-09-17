from unique_vals import *
unique_vals, cor = class_main()
print(f'unique: {unique_vals},\ncor: {cor}')


def yishay_calc(dic, userDic):
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
    buy *= cor['yes'] / sum(cor.values())
    not_buy *= cor['no'] / sum(cor.values())
    # print(f'buy {buy} , \nnot buy {not_buy}')
    return 1 if buy > not_buy else 0

a = ['youth','low','no','fair']
print(yishay_calc(unique_vals,a))

#print(yishay_calc(dic, userDic))