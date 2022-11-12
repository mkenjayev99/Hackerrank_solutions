income = int(input())

if income <= 100:
    fee = income*0.125 
elif 100 < income <=500:
    fee = income*0.1
elif 500 < income <= 1000:
    fee = income*0.075
else:
    fee = income*0.05

if fee*10%10 == 0:
    fee = int(fee)
print(fee)


