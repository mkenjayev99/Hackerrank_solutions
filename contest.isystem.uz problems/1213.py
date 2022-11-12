n = int(input())
nums = map(int, input().split())
nums = list(nums)
checker = []

for i in range(len(nums)):
    if nums[i] % 2 == 1:
        checker.append(1)
    else:
        checker.append(0)

if checker.count(1) == len(nums):
    print("ROST")
else:
    print("YOLG'ON")
