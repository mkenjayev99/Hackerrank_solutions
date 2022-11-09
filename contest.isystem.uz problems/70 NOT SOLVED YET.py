n = int(input())

arr = []
for i in range(n):
    imass = []
    for j in range(n):
        imass.append('.')
    arr.append(imass)
c= n-1
for i in range(n):
    for j in range(n):
        if arr[j][j] == arr[n-1][n-1]: # top-left to right-bottom ( \ )
            arr[j][j] = '*'
        if arr[i][j] == arr[i][n//2+1]: # middle-vertical ( | )
            arr[i][n//2] = '*'
        if arr[i][j] == arr[n//2][j]: # middle-horizontal ( - )
            arr[n//2][j] = '*'


for i in arr:
    print(i)