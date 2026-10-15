ip_adres = input("Введите адрес ")
part = ip_adres.split(".")
flag = True

if len(part) != 4:
    flag = False
else:
    for i in part:
        num = int(i)
        if num < 0 or num > 255:
            flag = False
            break
if flag:
    print("ДА")
else:
    print("НЕТ")
