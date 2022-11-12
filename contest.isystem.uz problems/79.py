n = int(input())

names = []
for i in range(n):
    name = input()
    names.append(name)

shorter = names[0]

for i in names:
    if len(i) < len(shorter):
        shorter = i

print(shorter)