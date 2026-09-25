stroka, stolb = map(int, input("Введите номер строки и столбца первой ячейки(через пробел): ").split())
stroka_2, stolb_2 = map(int, input("Введите номер строки и столбца второй ячейки(через пробел): ").split())
if abs(stroka - stolb) == abs(stolb_2 - stroka_2):
    print("YES")
# Проверка хода по диагонали
else:
    print("NO")
