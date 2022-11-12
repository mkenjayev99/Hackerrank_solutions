wieght, hieght = map(float, input().split())

bmi = wieght/(hieght**2)*10000

if bmi < 18.5:
    res = 'Underweight'
elif bmi >= 18.5 and bmi < 25:
    res = 'Normal weight'
elif bmi >= 25 and bmi < 30:
    res = 'Overweight'
elif bmi >= 30:
    res = 'Obese'

print(res)