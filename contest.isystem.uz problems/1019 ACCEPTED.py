goods = ["Shokolad", "Bulochka", "Pechenye", "Vafli", "Sok"]
good_codes = [1001, 1002, 1003, 1004, 1005]
good_costs = [10000, 12000, 8000, 20000, 14000]
code = int(input())
money = int(input())

if (code in good_codes) and (money >= good_costs[code-1001]):
    res = money - good_costs[code-1001]
    if res % 1000 < 500:
        res = res // 1000*1000
    elif res % 1000 >= 500:
        res = res // 1000*1000 + 1000

    five_thousand = res//5000
    thousand = (res - res//5000*5000)//1000

    print(f"{goods[code-1001]}\n{thousand} {five_thousand}")
else:
    exit()

