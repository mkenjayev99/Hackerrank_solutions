x = int(input())
sizes = list(map(int, input().split()))
n = int(input())
earned = 0
for line in range(n):
    shoe_size, cost = map(int, input().split())
    if shoe_size in sizes:
        earned += cost
        sizes.remove(shoe_size)
print(earned)