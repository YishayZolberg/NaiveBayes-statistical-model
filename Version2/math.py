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
    return buy > not_buy

#print(yishay_calc(dic, userDic))