# if __name__ == '__main__':
#     n = int(input())
#     t = tuple(map(int, input().split()))
#     print(hash(t))

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))