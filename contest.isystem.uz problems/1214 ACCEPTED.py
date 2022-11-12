n = int(input())
nums = map(int, input().split())
nums = list(nums)
c = 0
for i in nums:
    if i >= 10 and i < 100:
        c += i

print(c)