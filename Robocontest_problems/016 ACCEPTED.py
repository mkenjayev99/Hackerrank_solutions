from math import floor


a = [1000000000, 1000000, 1000, 100]
b = ['milliard ', 'million ', 'ming ', 'yuz ']
c = ['', "o'n ", 'yigirma ', "o'ttiz ", 'qirq ', 'ellik ', 'oltmish ', 'yetmish ', 'sakson ', "to'qson "]
d = ['', 'bir ', 'ikki ', 'uch ', "to'rt ", 'besh ', 'olti ', 'yetti ', 'sakkiz ', "to'qqiz "]

def say(n):
    for i in range(4):
        if n >= a[i]:
            return say(int(n//a[i])) + b[i] + say(int(round(n%a[i])))
    return c[int(floor(n/10))] + d[int(floor(n%10))]

n = int(input())
print(say(n))

