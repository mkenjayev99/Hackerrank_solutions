n = int(input())
nums = map(int, input().split())
nums = list(nums)
indx = []
c = 0
for i in range(len(nums)):
    if nums[i] == 0:
        indx.append(i)

for j in range(indx[0], indx[1]+1):
    c += nums[j]

print(c)