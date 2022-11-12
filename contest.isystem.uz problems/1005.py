a, b = map(int, input().split())
greater = a if a > b else b
lower = a if a < b else b

print(f"{greater//lower} {greater%lower}")
