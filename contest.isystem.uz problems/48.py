n, k = map(int, input().split()) # n => oobshe vaqt; k => 1 minutda nechtagacha ishchini o'lchash mumkinligi
lst = map(int, input().split()) # [i3], [i4], [i5], .... => 1 minutda nechta ishchi kelganligi
lst = list(lst)
# shundan: Nechta ishchi navbat kutib qoladi?
summ = sum(lst)
while n != 0:
    n -= 1
    summ -= k

if summ < 0:
    summ = 0
print(summ)