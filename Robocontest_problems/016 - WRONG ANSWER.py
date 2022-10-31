# dictuz = {'1':'bir', '2':'ikki', '3':'uch', '4':'to\'rt', '5':'besh', '6':'olti', '7':'yetti', '8':'sakkiz', '9':'to\'qqiz', 
# 'o\'n':'', '20':'yigirma', '30':'o\'ttiz', '40':'qirq', '50':'ellik', '60':'oltmish', '70':'yetmish', '80':'sakson', '90':'to\'qson',
# '100':'bir yuz', '1000':'bir ming', '1000000':'bir million', '1000000000':'bir milliard'
# }

# n = int(input())


# # n - > may be:
# #               a single digit num;  n >= 1 and n <= 9
# #               two-digit num;       n >= 10 and n <= 99
# #               three-digit num;     n >= 100 and n <= 999
# #               four-digit num;      n >= 1000 and n <= 9999
# #               five-digit num;      n >= 10000 and n <= 99999
# #               six-digit num;       n >= 100000 and n <= 999999
# #               seven-digit num;        ....   ....   ....
# #               eight-digit num;
# #               nine-digit num;
# #               ten-digit num;
# #               eleven-digit num;
# #               twelve digit num;    n >= 10^11 and n <= 10^12 - 1

# letters = ['bir', 'ikki', 'uch', 'to\'rt', 'besh', 'olti', 'yetti', 'sakkiz', 'to\'qqiz', 'o\'n', 'yigirma', 'o\'ttiz',
#  'qirq', 'ellik', 'oltmish', 'yetmish', 'sakson', 'to\'qson', 'bir yuz', 'bir ming', 'bir million', 'bir milliard', ]

# a = 123654987
# alist = [int(x) for x in str(a)]
# word = ''
# for i in alist:
#     if i == 1:
#         word += letters[0]
# # alist = []
# # for i in range(len(str(a))-1):
# #     a = a // 10
# #     alist.append(a)
# print(alist)
# * * * * * * * * * * * * * * * * * * * * * * * * * * *

from math import floor


a = [1000000000, 1000000, 1000, 100]
b = ['milliard ', 'million ', 'ming ', 'yuz ']
c = ['', "o'n ", 'yigirma ', "o'ttiz ", 'qirq ', 'ellik ', 'oltmish ', 'yetmish ', 'sakson ', "to'qson "]
d = ['', 'bir ', 'ikki ', 'uch ', "to'rt", 'besh ', 'olti ', 'yetti ', 'sakkiz ', "to'qqiz"]

def say(n):
    for i in range(4):
        if n >= a[i]:
            return say(int(round(n/a[i]))) + b[i] + say(int(round(n%a[i])))
    return c[int(floor(n/10))] + d[int(floor(n%10))]

n = int(input())
print(say(n))

