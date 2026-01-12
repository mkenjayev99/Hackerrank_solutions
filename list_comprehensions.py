if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

# 1ST WAY
ans = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                ans.append([i, j, k])
print(ans)

# 2ND WAY : one-liner
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])

# Or we can write the line like this:
print([[i, j, k]
       for i in range(x+1)
       for j in range(y+1)
       for k in range(z+1)
       if i + j + k != n])

