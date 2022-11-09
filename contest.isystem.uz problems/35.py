n = int(input())

scpaces = ' '*(n-1)
plot = '*'
 
for i in range(2*n-1):
    if i == n-1:
        scpaces = ''
        print(f"{plot}")
    elif i < n-1:
        print(f"{scpaces}{plot}")
        scpaces = scpaces[:-1]
        plot += '**'
    else: # i > (n*2-1)//2
        plot = plot[:-2]
        scpaces += ' '
        print(f"{scpaces}{plot}")


        
        