# user datas:
word = "H"
width = int(input())
length = (width*2)

# Top con:
for i in range(1, length):
    if i%2 != 0:
        print((word*i).center(width*2))

# Top pillars:
for i in range(width+1):
    print((word*width).center(length)+(word*width).rjust(length+width+width//2))

# Middle belt:
for i in range(width+1):
    if i%2 != 0:
        print((word*(width*5)).center((length+(width*4))))

# Bottom pillars:
for i in range(width+1):
    print((word*width).center(length)+(word*width).rjust(length+width+width//2))

# Bottom con:
for i in sorted(range(length), reverse=True):
    if i%2 != 0:
        print((word*i).center(width*10))


