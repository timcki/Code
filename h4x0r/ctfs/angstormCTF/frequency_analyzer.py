a = 'Pxevhfx mh tgzlmkhfvmy. Px ahix rhn xgchr hnk vmy. tvmy{utvd_mh_max_ynmnkx}.'
dic = {}

for char in a:
    if char not in dic.keys():
        dic[char] = 1
    dic[char] += 1

for w in sorted(dic, key=dic.get, reverse=True):
    print(w, dic[w])
