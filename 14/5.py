n = int(input("Сколько места в рюкзаке? "))
cennosti = list(map(int, input("Введите ценность предметов через пробел ").split()))

# Сортируем ценности по убыванию
cennosti.sort(reverse=True)

all = 0
for i in range(n):
    if i < len(cennosti) and cennosti[i] > 0:
        all += cennosti[i]

print("Максимаьная ценность предметов, помещающихся в рюкзак ", all)