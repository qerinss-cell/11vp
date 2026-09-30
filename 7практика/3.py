napitok = str(input("Введите номер напитка или его название:"))
count = int(input("Введите количество порций:"))
match napitok:
    case "1"|"Кофе":
        name_napitka = "Кофе☕"
        sena_sa_porziu = 120
        sena = sena_sa_porziu * count
    case "2" | "Чай":
        name_napitka = "Чай🍵"
        sena_sa_porziu = 80
        sena = sena_sa_porziu * count
    case "3" | "Сок":
        name_napitka = "Сок🧃"
        sena_sa_porziu = 100
        sena = sena_sa_porziu * count
    case "4" | "Вода":
        name_napitka = "Вода🫗"
        sena_sa_porziu = 50
        sena = sena_sa_porziu * count
    case "5" | "Лимонад":
        name_napitka = "Лимонад🍹"
        sena_sa_porziu = 90
        sena = sena_sa_porziu * count
    case _:
        name_napitka = "Ошибка,выберите корректный номер или название"
        sena_sa_porziu = 0
        sena = sena_sa_porziu * count
print(30*"-","КАФЕ",30*"-")
print(f"Название: {name_napitka}")
print(f"Количество порций: {count}")
print(f"Цена за одну порцию : {sena_sa_porziu}")
print("="*50)
print(f"Сумма к оплате : {sena}")
print("="*50)
print(60*"-")

