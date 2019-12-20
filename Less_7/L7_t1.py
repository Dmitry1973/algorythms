# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint
import copy


# создаем массив размера size и заполняем случайными целыми числами из диапазона [-100; 100)
size = 10
array = [randint(-100, 100) for x in range(size)]
array_a = copy.deepcopy(array)  # делаем глубокую копию, для проверки разными методами

# выводим исходный массив
print('*' * 30)
print('Initial array:')
print(array)
print('*' * 30)

print('Bubble sort')
n = 1
while n < len(array):
    for i in range(len(array) - n):
        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    n += 1
    print(array, f'\tn = {n-1}')

print('*' * 30)
print('Advanced bubble sort')


def bubble_sort_desc(array_a):

    swapped = True  # для прохода по массиву хотя бы один раз
    k = 0
    while swapped:

        swapped = False  # для прекращения проходов при отсутствии обмена эелементов
        for i in range(len(array_a) - 1):
            if array_a[i] < array_a[i + 1]:  # вправо всплывает самый "легкий" пузырь
                array_a[i], array_a[i + 1] = array_a[i + 1], array_a[i]
                swapped = True
        k += 1  # счетчик проходов
        print(array_a, f'\tn = {k}')

# функция с запоминанием обмена не всегда "выигрывает" у простого пузыря, надо позапускать раз несколько


bubble_sort_desc(array_a)
print('*' * 30)
