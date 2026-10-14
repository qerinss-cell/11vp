marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
count_5 = 0
count_2 = 0
for i in marks:
    if i == 5:
        count_5 += 1
    elif i == 2:
        count_2 += 1
print(f"Количество 5 - {count_5}, количество 2 - {count_2}")