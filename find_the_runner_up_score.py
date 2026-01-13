# 13.01.2026, 11.22

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arr = list(set(arr))
arr.sort()
arr.pop(-1)
print(arr.pop(-1))
