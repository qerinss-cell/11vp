import random
random_num = [random.randint(1, 100) for _ in range(5)]
min_num = min(random_num)
min_index = 0
print("Изначальный список", random_num)
for i in range(len(random_num)):
    if random_num[i] == min_num:
        min_index = i
        break

print("Минимальный элемент:", min_num, "под индексом:", min_index)

temp = random_num[0]
random_num[0] = random_num[min_index]
random_num[min_index] = temp

print("Список после обмена:", random_num)
