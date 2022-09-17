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
#print(yishay_calc(unique_vals,a))

#print(yishay_calc(dic, userDic))