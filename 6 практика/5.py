stroka, stolb = map(int, input("Введите номер строки и столбца первой ячейки(через пробел): ").split())
stroka_2, stolb_2 = map(int, input("Введите номер строки и столбца второй ячейки(через пробел): ").split())
# Ввод строк и столбов
if stroka == stroka_2 or stolb == stolb_2:
    print("YES")
# Проверка хода по вертикали или горизонтали
elif abs(stolb - stolb_2) == abs(stroka - stroka_2):
    print("YES")
# Проверка хода по диагонали
else:
    print("NO")
