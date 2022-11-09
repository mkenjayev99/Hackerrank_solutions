a = input()

coll = ''
if len(a) <5:
    a = a.zfill(5)
for i in a:
    if i == '0':
        coll += f'{i}!'
    elif i == a[-1]:
        coll += i
    else:
        coll += f'{i}!'

print(coll)
