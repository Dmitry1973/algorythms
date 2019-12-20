# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
import sys

a = 5
b = 6
c = a & b
d = a | b
e = a >> 2
f = a << 2

mass = (5, 6, 5 & 6, 5 | 6, 5 >> 2, 5 << 2)
print(mass)

print(f'a, b,\n5 & 6 = {c},\n5 | 6 = {d},\n5 >> 2 = {e},\n5 << 2 = {f}')

def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
      if hasattr(x, 'items'):
          for xx in x.items():
              show_size(xx, level +1)
      elif not isinstance(x, str):
          for xx in x:
              show_size(xx, level + 1)

show_size(f)

show_size(mass)

# 6 int чисел занимают 14 * 6 = 84 байта
# если все записать и произвести все операции внутри кортежа,
# то в итоге занимаемый размер одного кортежа будет 52 байта.
# второй вариант кода будет только строка 12, строки с 5 по 10 и последний принт - закоментировать