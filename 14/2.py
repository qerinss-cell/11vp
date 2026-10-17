import random

numbers = [[random.randint(1, 100) for j in range(random.randint(2, 5))]
           for i in range(random.randint(2, 5))]

print("Список:")
for row in numbers:
    print(row)

total = 0
max_sum = 0
max_row = 0

for i in range(len(numbers)):
    row_sum = 0
    for j in range(len(numbers[i])):
        row_sum += numbers[i][j]
    print("Сумма строки", i, "=", row_sum)
    total += row_sum
    if row_sum > max_sum:
        max_sum = row_sum
        max_row = i

print("Общая сумма:", total)
print("Строка с максимальной суммой:", max_row, "(сумма =", max_sum, ")")