#Вычислить расстояние между двумя точками на плоскости
from math import *
a=(3,5)
b=(6,9)
c=sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
print(c)
#Сгенерировать случайное число от 1 до 100
import random
h=random.randint(1,100)
print(h)
#Сгенерировать случайную точку на плоскости (координаты от -10 до 10) и вычислить расстояние от начала координат
x_dot=random.randint(-10,10)
y_dot=random.randint(-10,10)
start=sqrt(x_dot**2 + y_dot**2)
print(start)

