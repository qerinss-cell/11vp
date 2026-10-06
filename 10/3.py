max_num = 0
while True:
    num = int(input("Введите натуральное число "))
    if num > max_num:
        max_num = num
    if num == 0:
        break
print("Самое большое введенное число:", max_num)
