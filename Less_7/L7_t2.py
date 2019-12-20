# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import randint

# создаем массив [0, 50) случайных чисел

size = 13
array = [randint(0, 50) for x in range(size)]

print('*' * 30)
print('Initial array:')
print(array)
print('*' * 30)


def merge_sort(merged_arr: list):
    """
    функция делит поданный на вход массив,
    и рекурсивно все сортирует слиянием
    :param merged_arr: - список на входе
    :return: - список отсортированный слиянием на выходе
    """
    # если массив единичный,  то "приехали"
    if len(merged_arr) <= 1:
        return
    # разбиваем начальный массив на левую и правую части
    middle = len(merged_arr) // 2
    left = merged_arr[:middle]
    right = merged_arr[middle:]
    # рекуррентно их сортируем
    merge_sort(left)
    merge_sort(right)
    # "сливаем" левую и правые части
    comb_arr = merge(left, right)
    for i in range(len(merged_arr)):
        merged_arr[i] = comb_arr[i]
    return merged_arr


def merge(merge_1: list, merge_2: list):
    """
    Функция собирает из двух предварительно отсортированных массивов,
    поданных на вход, один и ео же возвращает
    :param merge_1: - первый отсортированный список
    :param merge_2: - второй отсортированный список
    :return: -  "слитый" из двух, отсортированный список
    """
    # заполняем дополнительный массив С нулями
    merged_arr = [0] * (len(merge_1) + len(merge_2))
    # объявляем и обнуляем счетчики
    i = k = n = 0
    # разбираем в С из А или В меньший элемент, пока какой-то из А или В не закончится
    while i < len(merge_1) and k < len(merge_2):
        if merge_1[i] <= merge_2[k]:
            merged_arr[n] = merge_1[i]
            i += 1
            n += 1
        else:
            merged_arr[n] = merge_2[k]
            k += 1
            n += 1
    # докладываем в С остатки из А или В - где осталось.
    while i < len(merge_1):
        merged_arr[n] = merge_1[i]
        i += 1
        n += 1
    while k < len(merge_2):
        merged_arr[n] = merge_2[k]
        k += 1
        n += 1
    return merged_arr


print('Merge sorted array:')
print(merge_sort(array))
print('*' * 30)
