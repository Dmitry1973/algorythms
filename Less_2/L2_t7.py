# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
import sys

n = int(input('введите n '))
res_1 = 0
for i in range(0, n+1):
    res_1 = res_1 + i
print(res_1)

res = n * (n + 1) / 2
print(int(res))


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__itet__'):
      if hasattr(x, 'items'):
          for xx in x.items():
              show_size(xx, level +1)
      elif not isinstance(x, str):
          for xx in x:
              show_size(xx, level + 1)


show_size(res)
show_size(int(res))

# как результат - необходимо было сохранить res как int, а не оставлять float.
# второй вариант кода здесь будет с заменой:
# res = int(n * (n + 1) / 2)