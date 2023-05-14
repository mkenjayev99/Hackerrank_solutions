n, m = map(int, input().split())
ptrn = ".|."  # pattern repetition

for i in range(n//2):
    print((ptrn*i).rjust((m-3)//2, "-")+ ptrn + (ptrn*i).ljust((m-3)//2, "-"))
print("WELCOME".center(m, "-"))
for i in range(n//2-1, -1, -1):
    print((ptrn*i).rjust((m-3)//2, "-")+ ptrn + (ptrn*i).ljust((m-3)//2, "-"))