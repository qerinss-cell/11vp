num_1 = int(input("Введите первое число "))
while True:
    num_2 = int(input("Введите второе число "))
    if num_2 > num_1:
        break
    else:
        print("Введите второе число снова ")
while True:
    num_3 = int(input("Введите третье число "))
    if num_2 < num_3:
        print("Последовательность принята")
        break
    else:
        print("Введите третье число снова ")




