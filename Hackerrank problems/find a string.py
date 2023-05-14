def count_substring(string, sub_string):
    sum = 0
    m = len(string)-(len(sub_string)-1)
    for i in range(m):
        if string.count(sub_string, i , i+len(sub_string)):
            # EXPLANATION: string.count(char or substring, start, end)
            sum = sum + 1
    return sum
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)