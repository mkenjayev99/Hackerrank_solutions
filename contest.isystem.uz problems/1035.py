n = int(input())

high = 6
low = 1
c = 0


for i in range(1, high+1):
    for j in range(high, low-1, -1):
        if i + j == n:
            c +=1

print(c)
