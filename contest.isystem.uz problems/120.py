n = int(input())

res = 'Oddiy yil'
if n % 400 == 0  or (n % 4 == 0 and n % 100 != 0):
    res = 'Kabisa yili'

print(res)