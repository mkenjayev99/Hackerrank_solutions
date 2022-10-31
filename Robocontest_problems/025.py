all_seconds = int(input())

hours = all_seconds//3600
if hours >= 24: # 181
    hours = hours%24
minutes = (all_seconds - hours*3600)//60
if minutes >= 60:
    minutes = minutes%60
seconds = all_seconds - hours*3600 - minutes*60
if seconds >= 60:
    seconds = seconds%60

_minutes = str(minutes).zfill(2)
_seconds = str(seconds).zfill(2)

print(f"{hours}:{_minutes}:{_seconds}")
