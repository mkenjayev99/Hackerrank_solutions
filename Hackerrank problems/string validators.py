'''
string.isalnum() can check what 
any LETTER or NUMBER exists in the string: 
Example:
>>> print 'ab123'.isalnum()  
True
>>> print 'ab123#'.isalnum()
False

string.isalpha() can check what 
any LETTER exists in the string: 
Example:
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

string.isdigit() can check what 
any NUMBER exists in the string: 
Example:
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

string.islower() returns "True" if 
    all letters in the string consist of 
    LOWERCASE LETTERS.
Example:
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

string.islower() returns "True" if 
    all letters in the string consist of 
    UPPERCASE LETTERS.
Example:
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
# False

any() -> iterable built-in function.
DESCRIPTION: The any() function returns True if 
any item in an iterable are true, otherwise it 
returns False. If the iterable object is empty, 
the any() function will return False. 
EXAMPLE: 
mylist = [False, True, False]
x = any(mylist)
print(x) #returns "True"

'''


if __name__ == '__main__':
    s = input()       

print(any([ l.isalnum() for l in s ]))
print(any([ l.isalpha() for l in s ]))
print(any([ l.isdigit() for l in s ]))
print(any([ l.islower() for l in s ]))
print(any([ l.isupper() for l in s ]))
