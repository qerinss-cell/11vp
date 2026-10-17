import random

numbers = [[random.randint(-10, 10) for j in range(random.randint(2, 5))]
           for i in range(random.randint(2, 5))]

print("Исходный список:",numbers)

filtered = []
for i in range(len(numbers)):
    row = []
    for j in range(len(numbers[i])):
        if numbers[i][j] > 0:
            row.append(numbers[i][j])
    filtered.append(row)

print("Отфильтрованный список:",filtered)
