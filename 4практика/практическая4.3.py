print("Введите 4х значное неотрицательное целое число")
chislo=int(input())
print("Цифра в позиции тысяч равна:")
s=chislo//1000
print(s)
print("Цифра в позиции сотен равна:")
d=(chislo//100)%10
print(d)
print("Цифра в позиции десятков равна:")
l=(chislo//10)%10
print(l)
print("Цифра в позиции единиц равна:")
v=chislo%10
print(v)