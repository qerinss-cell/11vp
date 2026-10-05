num = int(input("Введите число участников "))
count = 0   # счетчик людей между Александром и Левоном
found_first = False
i = 0

while i < num:
    name = input("Введите имя участника ")
    if name == "Александр" or name == "Левон":
        if not found_first:
            found_first = True
        else:
            break
    else:
        if found_first:
            count += 1
    i += 1

print("Количество человек между Александром и Левоном", count)
