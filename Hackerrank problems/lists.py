if __name__ == '__main__':
    N = int(input())

arr = []
commands = [ input().split(" ") for r in range(N) ]

for i in commands:
    cmd = i[0]
    if cmd == "print":
        print(arr)
    else:
        args = tuple( int(j) for j in i[1:] )
        eval("arr." + cmd + str(args))
