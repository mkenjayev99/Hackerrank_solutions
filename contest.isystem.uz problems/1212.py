n = map(int, input().split())
m = map(int, input().split())
k = map(int, input().split())
arr = []
arr.append(list(n))
arr.append(list(m))
arr.append(list(k))

result = 'NO MAGIC'
if (arr[0][0] + arr[1][1] + arr[2][2]) == arr[0][2] + arr[1][1] + arr[2][0] == \
    arr[0][0] + arr[0][1] + arr[0][2] == arr[1][0] + arr[1][1] + arr[1][2] == \
    arr[2][0] + arr[2][1] + arr[2][2] == arr[0][0] + arr[1][0] + arr[2][0] == \
    arr[0][1] + arr[1][1] + arr[2][1] == arr[0][2] + arr[1][2] + arr[2][2]:
    result = "MAGIC SON"

print(result)