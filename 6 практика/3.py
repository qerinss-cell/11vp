stroka, stolb = map(int, input("Введите номер строки и столбца первой ячейки(через пробел): ").split())
stroka_2, stolb_2 = map(int, input("Введите номер строки и столбца второй ячейки(через пробел): ").split())
color_1 = (stolb + stroka) % 2
color_2 = (stolb_2 + stroka_2) % 2
if color_1 == color_2:
    print("YES")
else:
    print("NO")
