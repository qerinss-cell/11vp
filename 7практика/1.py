reiting = int(input("Введите рейтинг продукта от 1 до 10:"))
match reiting:
    case 1 | 2 | 3 | 4:
        result = "Плохой продукт, не стоит пробовать"
        emoji = "😒"
    case  5 | 6 | 7:
        result = "Хороший продукт,можно попробовать"
        emoji = "😊"
    case 8 | 9 | 10:
        result = "Отличный продукт,стоит попробовать"
        emoji = "🤩"
    case _:
        result = "Ошибка, введите целое число от 1 до 10"
        emoji = "🫤"

print(f"Рейтинг: {reiting} - {result} {emoji}")
