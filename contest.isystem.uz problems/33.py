n = int(input()) # it maybe 10349
#                           
#                           5000 2
#                           1000 0
#                           500 0
#                           100 3
#                           50 0
#                           10 4
#                           5 1
#                           2 2
#                           1 0     
#                          

lst = [5000, 1000, 500, 100, 50, 10, 5, 2, 1]
how_much = []

for i in lst:
    if n // i != 0:
        how_much.append(n//i)
        n = n - n//i*i  #10349//5000 = 2*5000 = 10 000 => 10349 - 10 000 => n = 349
    else:
        how_much.append(0)
for i in range(len(how_much)):    
    print(f"{lst[i]} {how_much[i]}")