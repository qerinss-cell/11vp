numbers = [10, 20, 30, 40, 50]
num = int(input("Введите число: "))
flag = True
for i in range(len(numbers)):
    if num == numbers[i]:
        print("Такое число есть под индексом: ", i)
        flag = False
        break
if flag == 1:
    print("Нет такого числа")
