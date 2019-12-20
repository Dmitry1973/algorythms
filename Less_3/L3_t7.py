# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random

# создаем массив размера arr_size_7, с разбросом случайных значений от 0 до arr_size_7 ** 2
arr_size_7 = int(input('введите размер массива '))
array_7 = [random.randint(0, arr_size_7 ** 2) for i in range(arr_size_7)]
print(f'Начальный массив:\n{array_7}')

# список для минимумов
mins = []
min_7 = 0
k = 0
while k < 2:
    for i in range(len(array_7)):
        if array_7[i] < array_7[min_7]:
            min_7 = i
    mins.append(array_7[min_7])
    array_7.pop(min_7)
    k += 1

print(f'мин_1 = {mins[0]} \nмин_2 = {mins[1]}')
