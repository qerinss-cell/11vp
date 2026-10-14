word = str(input("Введите слово : "))
word = list(word)
reverse_word = word[::-1]

for i in word:
    for j in reverse_word:
        if i == j:
            polindrom = "Это палиндром"
        else:
            polindrom = "Это не палиндром"

print(polindrom)
