# To understand more about enumerate function, read this article:
# https://blog.hubspot.com/website/python-enumerate#:~:text=What%20does%20enumerate%20do%20in,the%20collection%20easier%20to%20access.
# 
# To understand more abut enumerat() class, read the documentation:
# https://docs.python.org/3/library/functions.html
# 
# DESCRIPTION to the code written below:
#    (kevin)
# 1. Reverse the given string and enumerate  it starting from 1.
# 2. do for "i", which stayed i, c in enumerated object, if c is one of "A", "E", "O", "U", "I"
# 3. Calculate the list which generated recently ^
# 4. Get the result into a variable named "kevin"
#    
#    (stuart)
# 5. calculate all `possibilities` using ```len(string)+1) * len(string)``` and 
#    get intact part of calculation after deviding it to 2.
# 6. Subtract the value (named "kevin") from calculated value and
#    load it into variable named "stuart"
# 
#    presenting the result:
# 7. print "Stuart <stuart's score here>" if value of stuart is bigger than kevin, 
#    otherwise print "Kevin <kevin's score here>";
#    if it is not both of above, then print "Draw"


def minion_game(string):
    kevin = sum(i for i, c in enumerate(reversed(string),1) if c in 'AEIUO')
    stuart = (len(string)+1) * len(string) // 2 - kevin

    if stuart>kevin:
        print(f"Stuart {stuart}")
    elif stuart<kevin: 
        print(f"Kevin {kevin}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)