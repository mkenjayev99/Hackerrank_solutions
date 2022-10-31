price = int(input())

all_price = map(int, input().split())
lst = list(all_price)

all_sum = sum(lst)

if all_sum >= price:
    print("Yes")
else:
    print("No")
