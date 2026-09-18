print("Введите количество учащихся")
Studend = int(input())
print("Введите количество мандаринов")
Mandarini = int(input())
mandarins_for_student= Mandarini // Studend
ostatki_mandarin = Mandarini % Studend
print("Сколько мандаринов достанется каждому:",mandarins_for_student)
print("Сколько мандаринов останется:",ostatki_mandarin)