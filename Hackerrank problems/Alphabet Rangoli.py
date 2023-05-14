alphabet = "abcdefghijklmnopqrstuvwxyz"

def print_rangoli(size):
    snip = alphabet[:size][::-1] # Slice `alphabet` from start to `size` and set it from `end` to `start`
    width = (((size * 2) - 1) * 2) - 1 # width is equal to (((size * 2) - 1) * 2) 
    rows = [] # create empty list for saving the answer
    for i in range(size):
        row_letters = snip[:i+1] # Snip `snip` from `start` to `loop index` (i) 
        row_letters += row_letters[::-1][1:] # Snip `row_letters` from end to start and begin with `1st index` 
        rows.append("-".join(row_letters).center(width, "-")) # add `row_letters` to "-" <string> and set it to center with "-" for `width` distance
    rows = rows + rows[:size-1][::-1] # add `reversed` half of answer which stayed in rows[] to rows[]
    print("\n".join(rows))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)