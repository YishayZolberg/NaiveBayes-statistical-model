




dic = {'age': {'middle_age': {'yes': 0, 'no': 4}, 'senior': {'yes': 3, 'no': 2}, 'youth': {'yes': 2, 'no': 3}},
'income': {'high': {'yes': 2, 'no': 22}, 'medium':{'yes': 4, 'no': 2}, 'low':{'yes': 3, 'no': 1}},
'student': {'yes': {'yes': 0, 'no': 1}, 'no': {'yes': 18, 'no': 5}}}

userDic = ['middle_age','high','no']

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
            templen += 1
            yes += 1
        if no == 0:
            templen += 1
            no += 1
        print(templen, yes, no)
        if buy == 0.0:
            buy = yes / templen
        else:
            buy *= yes / templen

        if not_buy == 0.0:
            not_buy = no / templen
        else:
            not_buy *= no / templen

    return buy > not_buy

print(yishay_calc(dic, userDic))
