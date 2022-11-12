nums = map(int, input().split())
nums = list(nums)
act = input().split()
act = list(act)
c = ''
c += str(nums[0])
c += act[0]
c += str(nums[1])
c += act[1]
c += str(nums[2])

print(int(eval(c)))