if __name__ == '__main__':
    n = int(input())

num = 0
for i in range(1, n+1):
    power = 0
    j = i
    while j%10 != 0 or j//10 != 0:
        power +=1
        j //= 10
    num *= 10**power
    num += i

print(num)