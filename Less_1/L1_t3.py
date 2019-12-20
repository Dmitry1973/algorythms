# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

z1 = int(input('введите первое целое число '))
z2 = int(input('введите второе целое число '))
r1 = float(input('введите первое вещественное число '))
r2 = float(input('введите второе вещественное число '))
alpha1 = ord(input('введите первый латинский символ '))
alpha2 = ord(input('введите второй латинский символ '))

if z1 > z2:
    int_random = random.randint(z2, z1)
else:
    int_random = random.randint(z1, z2)
print(f'случайное целое между {z1} и {z2} = {int_random}')

real_random = random.uniform(r1, r2)
print(f'случайное вещественное между {r1} и {r2} = {real_random}')

if alpha1 > alpha2:
    alpha_random = random.randint(alpha2, alpha1)
else:
    alpha_random = random.randint(alpha1, alpha2)

alpha = chr(alpha_random)
print(f'случайный символ между {chr(alpha1)} и {chr(alpha2)} = {alpha}')
