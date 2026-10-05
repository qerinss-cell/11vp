num = int(input("Введите число "))
count_3 = 0
last = num % 10
count_last = 0
count_chet = 0
count_0_and_5 = 0
proisvedenie_7 = 1
summ_more_when_5 = 0
while num > 0:
    n = num % 10
    if n == 3:
        count_3 += 1
    if n % 2 == 0:
        count_chet += 1
    if n > 5:
        summ_more_when_5 += n
    if n > 7:
        proisvedenie_7 *= n

    if n == 0 or n == 5:
        count_0_and_5 += 1

    if n == last:
        count_last += 1
    num //= 10
if proisvedenie_7 == 1:
    proisvedenie_7 = 0

print("Количество цифр 3:", count_3)
print("Сколько раз встречается последняя цифра:", count_last)
print("Количество четных цифр :", count_chet)
print("Сумма цифр больше 5:", summ_more_when_5)
print("Произведение цифр больше 7:", proisvedenie_7)
print("Количество цифр 0 и 5:", count_0_and_5)

