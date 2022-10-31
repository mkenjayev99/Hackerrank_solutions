# TIME LIMIT - ERROR CODE

# n = int(input())
# lst = list(range(1, n+1))

# primes = 0
# for i in range(2, n+1):
#     c = 0
#     for j in range(2, i+1):
#         if i % j == 0:
#             c += 1
#     if c <= 2:
#         primes += 1
# if primes % 2 == 0:
# 	print("Bobur")
# else:
# 	print("Ali")

# TIME LIMIT - ERROR CODE

# n = int(input())
# lst = list(range(1, n+1))
# prime_nums = 0

# for i in range(2, n+1):
#     c = 0
#     for j in range(2, n+1):
#         if i % j == 0:
#             c += 1
#     if c == 1:
#         prime_nums += 1

# if prime_nums % 2 == 0:
#     print("Bobur")
# else:
#     print("Ali")


# TIME LIMIT - ERROR CODE

# num_list = list(range(1, int(input()) + 1))
# primes = [1 if num > 1 and len([i for i in range(2, int(num / 2+1)) if num % i == 0]) == 0 else 0 for num in num_list]

# c = 0
# for i in primes:
#     if i == 1:
#         c += 1

# print("Ali") if c % 2 == 1 else print("Bobur")