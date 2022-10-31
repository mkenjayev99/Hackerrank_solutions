# def leapYear(y):
#     ans = False
#     if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
#         ans = True
#     return ans
# q = int(input())
# print(f"year: {q}  ", leapYear(q))



# def dayOfProgrammers(year):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         return f"12.09.{year}"
#     else:
#         return f"13.09.{year}"
# y = int(input())
# print(dayOfProgrammers(y))


# import math, random, re, sys, os

# def dayOfProgrammaer(year):
#     if year == 1918:
#         answer = '26.09.1918'
#     elif (year <= 1917 and year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#         answer = f'12.09.{year}'
#     else:
#         answer = f'13.09.{year}'
#     return answer



# def dayOfProgrammer(year):
#     febLeapYearDays = 29
#     month = 9
#     monthDaystoAugust = [31, 28, 31, 30, 31, 30, 31, 31]

#     if year <= 1917 :
#         if year % 4 == 0 :
#             monthDaystoAugust[1] = febLeapYearDays


#     elif year >= 1919 :
#         if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) :
#             monthDaystoAugust[1] = febLeapYearDays

#     else:
#         monthDaystoAugust[1] = 15

#     _day = str(256 - sum(monthDaystoAugust)).zfill(2)
#     _year = str(year).zfill(4)
#     _month = str(month).zfill(2)

#     return f"{_day}.{_month}.{_year}"

# q = int(input())
# print(dayOfProgrammer(q))

def dayOfProgrammer(year):
    _year = str(year).zfill(4)
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        answer = f'12/09/{_year}'
    else:
        answer = f'13/09/{_year}'
    return answer

q = int(input())
print(dayOfProgrammer(q))
