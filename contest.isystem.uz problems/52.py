a, b = map(str, input().split())

if float(a)*10 % 10 != 0 and float(b)*10 % 10 != 0:
    print(True)
else:
    print(False)
