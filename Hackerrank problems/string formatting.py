# 
#   Space = 6
# Decimal | Octal | Hexadcimal | Binary

#     1        1          1          1
#     2        2          2         10
#     3        3          3         11
#     4        4          4        100
#     5        5          5        101
#     6        6          6        110
#     7        7          7        111
#     8       10          8       1000
#     9       11          9       1001
#    10       12          A       1010
#    11       13          B       1011
#    12       14          C       1100
#    13       15          D       1101
#    14       16          E       1110
#    15       17          F       1111
#    16       20         10      10000
#    17       21         11      10001

        # 1ST WAY ==> EXCEEDED ERROR 
# def print_formatted(number):
#     space = len(bin(number)[2:])
#     decimal = list(range(1, number+1))
#     octal = [oct(i)[2:] for i in decimal]
#     hexadecimal = [hex(i)[2:] for i in decimal]
#     binary = [bin(i)[2:] for i in decimal]
#     for i in range(number):
#         print(str(decimal[i]).rjust(space, ' ')+ ' ' + str(octal[i]).rjust(space, ' ')+ ' ' + str(hexadecimal[i]).rjust(space, ' ')+ ' ' + str(binary[i]).rjust(space, ' '))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)





def print_formatted(number):
    space = len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(space, ' '), end=' ')
        print(oct(i)[2:].rjust(space, ' '), end=' ')
        print(hex(i)[2:].upper().rjust(space, ' '), end=' ')
        print(bin(i)[2:].rjust(space, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
