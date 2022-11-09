h, m, s = map(int, input().split())
h2, m2, s2 = map(int, input().split())

time1 = h*3600 + m*60 + s
time2 = h2*3600 + m2*60 + s2

print(abs(time1 - time2))