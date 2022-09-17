from unique_vals import *
unique_vals, dict_corl = class_main()
#print(f'unique: {unique_vals},\ncor: {cor}')


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
    buy *= dict_corl['yes'] / sum(dict_corl.values())
    not_buy *= dict_corl['no'] / sum(dict_corl.values())
    # print(f'buy {buy} , \nnot buy {not_buy}')
    return 1 if buy > not_buy else 0

#a = ['youth','low','no','fair']
#print(yishay_calc(unique_vals,a))

#print(yishay_calc(dic, userDic))