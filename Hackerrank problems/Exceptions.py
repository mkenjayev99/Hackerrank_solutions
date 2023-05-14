# 1ST WAY

# n = int(input())
# res = []
# for num in range(n):
#     a, b = input().split()
#     try:
#         if b.isalnum() and a.isalnum():
#             res.append(int(a)//int(b))
#         else:
#             if not b.isalnum():
#                 res.append(f"Error Code: invalid literal for int() with base 10: '{b}'")
#             elif not a.isalnum():
#                 res.append(f"Error Code: invalid literal for int() with base 10: '{a}'")

#     except ZeroDivisionError:
#         res.append("Error Code: integer division or modulo by zero")

# print(*res, sep='\n')

# 2ND WAY:

T = int(input())
result = []
for i in range(T):
    try:
        a,b=map(int,input().split())
        result.append(a//b)
    except Exception as e:
        result.append(e)
for i in result:
    if type (i) == int:
        print(i)
    else:
        print("Error Code:",i)