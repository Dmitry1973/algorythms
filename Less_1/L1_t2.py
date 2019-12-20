# 2. По введенным пользователем координатам двух точек вывести уравнение прямой вида  𝑦=𝑘𝑥+𝑏 ,
# проходящей через эти точки.
import sys

# x1 = float(input('введите координату х1: '))
# y1 = float(input('введите координату y1: '))
# x2 = float(input('введите координату х2: '))
# y2 = float(input('введите координату y2: '))

x1 = 1
x2 = 2.0
y1 = 5.5
y2 = 4

if x1 != x2:
    k = round((y2 - y1) / (x2 - x1), 2)
    b = round(y1 - k * x1, 2)
    if y1 != y2:
        print(f'y = {k}*x + {b}')
    else:
        print(f'y = {b}')
else:
    print(f'x = {x1}')
var = [x1, x2, y1, y2]

# for i in enumerate(var):
#     print(i)
#     print(id(i))
#     print(sys.getsizeof(i))
#
# print(id(var))
# print(sys.getsizeof(var))

# for value in vars().values(): print(value)

print(id(vars()))
print(sys.getsizeof(vars().keys()))
print(sys.getsizeof(vars().values()))