# подсчет памяти под переменные в программах

import  sys


def sum_memory(objects, verbose=True):
    sum_mem = 0
    for item in objects:
        if item.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(objects[item], '__call__'):
            # убираем функции
            continue
        elif hasattr(objects[item], '__loader__'):
            # убираем модули
            continue
        else:
            sum_mem += sys.getsizeof((objects[item]))
            if verbose:
                print(f'Переменная = {item};\tкласс = {type(objects[item])};\tзначение = {objects[item]};'
                      f'\tханимает {sys.getsizeof(objects[item])} байт(а)')

    return f'Переменные заняли {sum_mem} байт(а)'

# вызов функции подсчета в таком виде:
# locals() - "забирает" локальные переменные и подсчитывает занимаемую ими память
# print (sum_memory(locals(), verbose=True)
