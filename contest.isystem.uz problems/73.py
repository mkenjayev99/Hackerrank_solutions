letter = input()
word = input()

word_lst = list(word)

for i in range(3, len(word_lst), 3):
    if word_lst[i] == letter:
        word_lst[i] = letter.upper()
    else:
        word_lst[i] = '*'

for i in range(len(word_lst)):
    print(word_lst[i], end='')

