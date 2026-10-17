lyt = list(map(int, input("Введите стоимость предметов через пробел ").split()))

# По возрастанию цены
up = sorted(lyt)

#  По убыванию цены
down = sorted(lyt, reverse=True)

# Оригинальный порядок
original = lyt[:]

# Обратный порядок
back = lyt[::-1]

print("Сортировка по возрастанию:", up)
print("Сортировка по убыванию:", down)
print("Оригинальный порядок :", original)
print("Обратный порядок :", back)