# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
import sys

num = input('введите число ')
inverse_num = ''
for i in num:
    inverse_num = i + inverse_num
print(inverse_num)
# если надо целое, а не строка, раскомментировать строки ниже
# inv_num = int(inverse_num)
# print(inv_num)
print(sys.getsizeof(num))