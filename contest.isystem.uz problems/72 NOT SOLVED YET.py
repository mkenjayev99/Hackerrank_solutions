n = int(input())
star = '*'
space = ''
space_const = ' '
if n == 1:
    print(f"{star}{space}")
    space += ' '
    print(f"{space}{star}")
    space = ''
    print(f"{star}{space}")

else:
    res_const = '***'
    print(res_const)
    for i in range(n+2):
        space += ' '
        if i >= (n+2)//2:
            space = space[:-1]
        print(f"{space}{star}{space_const}{star}")
    print(res_const)
    
    

    
    