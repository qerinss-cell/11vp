import random

numbers = [[random.randint(1, 100) for j in range(random.randint(2, 5))]
           for i in range(random.randint(2, 5))]

print("Список:")
for row in numbers:
    print(row)

max_elem = numbers[0][0]
max_i = 0
max_j = 0

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] > max_elem:
            max_elem = numbers[i][j]
            max_i = i
            max_j = j

print("Максимальный элемент:", max_elem)
print("Индекс строки:", max_i)
print("Индекс позиции в строке:", max_j)