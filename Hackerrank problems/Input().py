# 1st way
# x, k = map(int, input().split())
# expression = input().replace("x", str(x))
# print(True if eval(expression) == k else False)

# 2nd way
x, k = map(int, input().split())
print(eval(input()) == k)

# 'x**3 + x**2 + x + x' => python already knows that x = 1. Cause we told (inputted) it before.
