# from itertools import permutations
# word, num = sorted(input().upper()), int(input())
# for i in permutations(word, num):
#     print(''.join(i))

from itertools import permutations
word, k = input().split()
word, k = sorted(word.upper()), int(k)
for i in permutations(word, k):
    print(''.join(i))