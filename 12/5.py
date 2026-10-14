data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_trika = data[:3]
print("Первая тройка чисел ", *first_trika)

last_troika = data[-3:]
print("Последняя тройка чисел", *last_troika)

reverse = data[::-1]
print("Список в обратном порядке: ", *reverse)

nechet_index = data[1::2]
print("Только элементы с нечетными индексами", *nechet_index)
