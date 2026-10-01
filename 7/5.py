num = int(input("Введите количество чисел: "))

max1 = 0
max2 = 0

for i in range(num):
    chislo = int(input(f"Введите число {i + 1}: "))
    if chislo > max1:
        max2 = max1
        max1 = chislo
    elif chislo > max2:
        max2 = chislo

print("Наибольшее:", max1)
print("Второе по величине:", max2)