# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import sys

# создаем массив размера arr_size, с разбросом случайных значений от 0 до arr_size_6 ** 2
arr_size_6 = int(input('введите размер массива '))
array_6 = [random.randint(0, arr_size_6 ** 2) for i in range(arr_size_6)]
print(f'Начальный массив:\n{array_6}')

# определяем мин, макс значения и их индексы
min_6 = 0
max_6 = 0
for i in range(arr_size_6):
    if array_6[i] < array_6[min_6]:
        min_6 = i
    elif array_6[i] > array_6[max_6]:
        max_6 = i

# индекс начинается с 0!
print('\nиндексы начинаются с 0!')
print(f'array_min[{min_6}] = {array_6[min_6]} \narray_max[{max_6}] = {array_6[max_6]}')
sum_6 = 0

# array_6 = tuple(array_6)

# проверяем какой индекс больше
if min_6 < max_6:
    for i in range(min_6 + 1, max_6):
        sum_6 = sum_6 + array_6[i]
else:
    for i in range(max_6 + 1, min_6):
        sum_6 = sum_6 + array_6[i]

print(f'сумма чисел между мин и макс = {sum_6}')


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
      if hasattr(x, 'items'):
          for xx in x.items():
              show_size(xx, level +1)
      elif not isinstance(x, str):
          for xx in x:
              show_size(xx, level + 1)

show_size(sum_6)

show_size(array_6)

# если оставить массив в виде списка - память занимает 136 байт
# если пересохранить в кортеж - 108
# второй варианг кода - с раскомментированной строкой 26