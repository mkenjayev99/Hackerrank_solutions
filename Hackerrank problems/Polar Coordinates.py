# print(*exp) and print(exp) <== what is diffirence?
# if exp = (2.23606797749979, 1.1071487177940904), 
# 1st prints it as 2.23606797749979 1.1071487177940904 that is, without any commas or quotation marks.
# 2nd prints it as (2.23606797749979, 1.1071487177940904) that is, as it is.


import cmath
print(*cmath.polar(complex(input())), sep="\n")


exp = input()
exp = complex(exp)
print(exp)
exp = cmath.polar(exp)
print(*exp)
