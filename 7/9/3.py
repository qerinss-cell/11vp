price = int(input("Введите цену услуг ведьмака "))
count_25 = 0
count_10 = 0
count_5 = 0
count_1 = 0
while price > 0:
    if price >= 25:
        count_25 += 1
        price -= 25
    elif price >= 10:
        count_10 += 1
        price -= 10
    elif price >= 5:
        count_5 += 1
        price -= 5
    elif price >= 1:
        count_1 += 1
        price -= 1
sum_monet = count_25 + count_1 + count_5 + count_10
print(f"Вам необходимо дать ведьмаку всего {sum_monet} монет/ы ")
print(f"монеты номиналом 25: {count_25}")
print(f"монеты номиналом 10: {count_10}")
print(f"монеты номиналом  5:{count_5} ")
print(f"монеты номиналом  1:{count_1}")
