a = int(input())
nums = map(int, input().split())

lst = list(nums)
lst = sorted(lst)
c = 0
for i in lst:
    if i > 0:
        c +=1

print(c)