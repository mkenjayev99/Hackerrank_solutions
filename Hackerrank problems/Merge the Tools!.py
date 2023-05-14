from textwrap import wrap

def merge_the_tools(string, k):
    wrapped_list = wrap(string, width=k)
    for sub_str in wrapped_list:
        print(''.join(list(dict.fromkeys(sub_str))))

# sub_str = 'aaabbbc'
# ''.join(list(dict.fromkeys(sub_str)))
# returns non-repetetion characters-contained string

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)