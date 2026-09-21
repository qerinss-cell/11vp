from math import *
x_degrii = float(input())
x_radian = math.radians(x_degrii)
result = math.sin(x_radian) + math.cos(x_radian) + math.tan(2 * x_radian)
print(result)