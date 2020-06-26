# -*- coding:utf-8 -*-
def countn(s: str):

    dic = {}
    for i in range(len(s)):
        dic[s[i]] = s.count(s[i])
    return dic


ss = input()
print(countn(ss))
