# calendar.weekday(year, month, day)
# Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).
from calendar import weekday, day_name
month, day, year = map(int, input().split())
print(day_name[weekday(year, month, day)].upper())