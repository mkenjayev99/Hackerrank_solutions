n, m = map(int, input().split())

def Solve(n, m):
 
    X_axis = []
    X_axis = [-2, -1, 1, 2]
    Y_axis = []
    Y_axis = [1, 2, 2, 1]
 
    ret = 0
 
    for i in range(m):
        for j in range(n):
            for k in range(4):
 
                x = i + X_axis[k]
                y = j + Y_axis[k]
 
                if (x >= 0 and x < m and
                        y >= 0 and y < n):
                    ret += 1
 
    Total = m * n
    Total = Total * (Total - 1) // 2
 
    return 2 * (Total - ret)
 
print(Solve(n, m))

# I soved the problem with copy-paste method. Now, I must to know how it works.