# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

# для пользовательского ввода, раскомментировать строку 12 и закомментировать 13
m = (int(input('введите int m ')))
n = m + 1
size = 2 * m + 1
# size = 3
# заполняем массив случайными целыми числами
array = [random.randint(-size * 10, size * 10) for x in range(size)]

print(array)


def quickselect_median(array, pivot_fn=random.choice):
    if len(array) % 2 == 1:
        return quickselect(array, len(array) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(array, len(array) / 2 - 1, pivot_fn) +
                      quickselect(array, len(array) / 2, pivot_fn))


def quickselect(array, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param array: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot (опорная), по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(array) == 1:
        # assert k == 0
        return array[0]

    pivot = pivot_fn(array)

    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


print("медиана массива (поиск без сортировки) =", quickselect_median(array))

# сортировка кучей


def heapify(arr, n, i):
    """
    преобразование массива в двоичную кучу поддервеа с корменыйм узлом i,
    что является индексом в arr[]

    :param arr: массив для преобразований
    :param n: - размер кучи
    :param i: - индекс массива
    :return: - преобразованный массиы
    """
    largest = i  # инициализация корня
    left = 2 * i + 1
    right = 2 * i + 2

    # проверка, если левый дочерний элемент существует и
    # больше ли он корня
    if left < n and arr[i] < arr[left]:
        largest = left

    # проверка, если правый дочерний элемент существует и
    # больше ли он корня
    if right < n and arr[largest] < arr[right]:
        largest = right

    # замена корня, если требуется
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

    # Heapify the root.
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # построение кучи
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # по одному, извлечение элементов
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # смена мест
        heapify(arr, i, 0)


heap_sort(array)
print('*' * 30)
print('Heap sorted array:')
print(array)
print("медиана массива (через сортировку кучей) =", array[m])



