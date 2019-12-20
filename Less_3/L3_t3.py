# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

# создаем массив размера n, с разбросом случайных значений от 0 до n * n
n = int(input('введите размер массива '))
array_3 = [random.randint(0, n * n) for i in range(n)]
print(f'Начальный массив:\n{array_3}')

# определяем мин, макс значения и их индексы
min_3 = 0
max_3 = 0
for i in range(n):
    if array_3[i] < array_3[min_3]:
        min_3 = i
    elif array_3[i] > array_3[max_3]:
        max_3 = i

# индекс начинается с 0!
print('\nиндексы начинаются с 0!')
print(f'array_min[{min_3}] = {array_3[min_3]} \narray_max[{max_3}] = {array_3[max_3]}')

# меняем местами мин и макс значения
array_3[min_3], array_3[max_3] = array_3[max_3], array_3[min_3]

# вывод измененного массива
print(f'\nИзмененный массив:\n{array_3}')


