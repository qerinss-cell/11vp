summa = 0
while True:
    price = int(input("Введите стоимость товара "))
    if price < 0:
        print("Ошибка цены")
        continue
    if price == 0:
        break
    summa += price
if summa > 1000:
    summa = summa - summa * 0.1
print(summa)
