hour1, minut1, second1 = map(int, input().split())
hour2, minut2, second2 = map(int, input().split())

all_secsonds1 = hour1*3600 + minut1*60 + second1
all_secsonds2 = hour2*3600 + minut2*60 + second2

print(abs(all_secsonds1-all_secsonds2))
