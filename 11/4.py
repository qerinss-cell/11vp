n = int(input("Введите число "))

last_digit = n % 10
temp = n

count_3 = 0
count_last = 0
count_even = 0
sum_more_5 = 0
product_more_7 = 1
count_0_and_5 = 0

while temp > 0:
    digit = temp % 10

    if digit == 3:
        count_3 += 1

    if digit == last_digit:
        count_last += 1

    if digit % 2 == 0:
        count_even += 1

    if digit > 5:
        sum_more_5 += digit

    if digit > 7:
        product_more_7 *= digit

    if digit == 0 or digit == 5:
        count_0_and_5 += 1

    temp = temp // 10

print("Количество троек",count_3)
print("Сколько раз встречается последняя цифра",count_last)
print("количество чётных цифр",count_even)
print("сумма цифр, больших пяти",sum_more_5)
print("произведение цифр, больших семи",product_more_7)
print("сколько раз в нём встречаются цифры 0 и 5",count_0_and_5)