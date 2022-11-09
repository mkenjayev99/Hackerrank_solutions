n, m = map(int, input().split())

def Solve(n, m):

    x_axis = [-2, -1, 1, 2]
    y_axis = [1, 2, 2, 1]

    cou = 0

    for i in range(m):
        for j in range(n):
            for k in range(4):
                x = i + x_axis[k]
                y = j + y_axis[k]

                if (x>=0 and x<m and y>=0 and y<n):
                    cou += 1

    total = m*n
    total = total*(total -1)//2
    
    return 2*(total - cou)

print(Solve(n, m))