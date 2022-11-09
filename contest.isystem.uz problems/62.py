n = int(input())
nums = map(int, input().split())

num_lst = list(nums)
c = 0
sp = 1
for i in num_lst:
    for j in num_lst[sp:]: # every loop will starts with new target
        if i == j:
            c +=1
    sp +=1 # DO THIS FOR SETTING A NEW TARGET
print(c)
