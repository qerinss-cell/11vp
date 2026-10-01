chotnie = True
k = 1
for i in range(10):
    n = int(input(f"Введите число {k}: "))
    k += 1
    if n % 2 != 0:
        chotnie = False

print("YES" if chotnie else "NO")