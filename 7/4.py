m = int(input("стартовое количество организмов "))
p = float(input("среднесуточное увеличение в процентах "))
n = int(input("количество дней для размножения "))
number = 0
for i in range(1,n+1):
    m = m+(m*p)
    number += 1
    print(f" {number} {m:.2f}")
