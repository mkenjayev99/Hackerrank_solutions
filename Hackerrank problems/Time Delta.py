# description for ``` time_format = "%a %d %b %Y %H:%M:%S %z" ```:
# %a => day name; %d => day number; %Y => year; %H:%M:%S => hour:minute:secoond; %z => timezone

#!/bin/python3
from datetime import datetime

def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"

    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)

    return str(int(abs((t1-t2).total_seconds())))


t = int(input())

delta = []
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta.append(time_delta(t1, t2))
print(*delta, sep='\n')
