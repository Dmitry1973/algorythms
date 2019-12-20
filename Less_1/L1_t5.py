# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
from Less_6 import Memory_sum

num = int(input('введите число от 1 до 26 включительно '))
shift5 = ord('a') - 1
alpha5 = chr(num + shift5)
print(f'числу {num} соответствует буква "{alpha5}"')

s_m = Memory_sum.SumMemory()
s_m.extend(num, shift5, alpha5)
s_m.prin_sum()