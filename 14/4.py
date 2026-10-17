import random

numbers = [[random.randint(1, 10) for j in range(random.randint(2, 5))]
           for i in range(random.randint(2, 5))]

chislo = random.randint(1, 10)

print("Список:", numbers)

print("Ищем значение:", chislo)

found = False
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] == chislo:
            print("Найдено в позиции: строка", i, ", столбец", j)
            found = True

if not found:
    print("Элемент не найден")