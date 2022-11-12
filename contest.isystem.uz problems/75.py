n = int(input())


def decimalToBinary(n):
    return bin(n).replace("0b", "")

bin_lst = list(decimalToBinary(n))
print(bin_lst.count(str(1)))