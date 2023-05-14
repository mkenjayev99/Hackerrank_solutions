# To understand more about defaultdict() function (or subclass), read this article:
# https://realpython.com/python-defaultdict/#:~:text=The%20Python%20defaultdict%20type%20behaves,handling%20missing%20keys%20in%20dictionaries.
# 

from collections import defaultdict

A = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n+1):
    A[input()].append(str(i))

for _ in range(m):
    val = input()
    if val in A:
        print(" ".join(A[val]))
    else:
        print(-1)