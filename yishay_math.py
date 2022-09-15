




dic = {'age': {'middle_age': {'yes': 5, 'no': 4}, 'senior': {'yes': 3, 'no': 2}, 'youth': {'yes': 2, 'no': 3}},
'income': {'high': {'yes': 2, 'no': 22}, 'medium':{'yes': 4, 'no': 2}, 'low':{'yes': 3, 'no': 1}},
'student': {'yes': {'yes': 0, 'no': 1}, 'no': {'yes': 18, 'no': 5}}}

userDic = ['middle_age','high','no']

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
    print(buy)
    print(not_buy)
    return buy > not_buy

print(yishay_calc(dic, userDic))
