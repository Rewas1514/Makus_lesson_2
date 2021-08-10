money_list = [50, 25.3, 100.1, 29, 41.3, 29.5, 11.1, 44.3, 55, 87.3, 81, 13.8]
for money in money_list:
    rub = int(money)
    kop = (money - int(money)) * 100
    print(f'{rub} рублей {kop:02.0f} копеек')    # добавляем нули ,0f - округление 0 знаков после запятой

money_list = [50, 25.3, 100.1, 29, 41.3, 29.5, 11.1, 44.3, 55, 87.3, 81, 13.8]
print(id(money_list))
money_list.sort()
print(money_list)
for money in money_list:
    rub = int(money)
    kop = (money - int(money)) * 100
    print(f'{rub} рублей {kop:02.0f} копеек')