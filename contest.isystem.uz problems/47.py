a, b, c = map(int, input().split())
if a == (a**2 + c**2)**(1/2) or b == (a**2 + c**2)**(1/2) or c == (a**2 + b**2)**(1/2):
    print("ture")
else:
    print("false")
