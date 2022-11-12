n = int(input())
nums = map(int, input().split())
nums = list(nums)

for i in nums:
    if nums.count(i) >=2:
        print('SONLAR ORASIDA TAKRORLANISH MAVJUD')
        break