status = str(input("Введите статус заказа изпредложенных:pending,processing,shipped,delivered,cancelled:"))
match status:
    case "pending":
        result, emoji, opisanie, data = ("В ожидании", "🫣", "Заказ ожидает оплаты", "40-60 минут")
    case "processing":
        result, emoji, opisanie, data = ("В обработке", "🤗", "Заказ находится в обработке", "30-40 минут")
    case "shipped":
        result, emoji, opisanie, data = ("отправлено", "🎆", "Заказ передан в доставку", "1-2 недели")
    case "delivered":
        result, emoji, opisanie, data = ("доставлено", "😍", "Заказ находится в пункте выдачи", "заберите в течение 2-х недель")
    case "cancelled":
        result, emoji, opisanie, data = ("отменено", "🤷‍", "Заказ отменен", "-")
    case _:
        result, emoji, opisanie, data = ("Ошибка", "❌‍", "invalid_status, доступные статусы:pending, processing, shipped, delivered, cancelled", "-")

print(30*"=", "🚩СТАТУС ВАШЕГО ЗАКАЗА🚩", 30*"=")
print(f"Статус:{result}{emoji}")
print(f"Описание:{opisanie}")
print(f"Время ожидания:{data}")
print(60*"=")
