n = int(input())
nums = map(int, input().split())
nums = list(nums)
summ = 0
for i in nums:
    summ += i**3
print(summ)
