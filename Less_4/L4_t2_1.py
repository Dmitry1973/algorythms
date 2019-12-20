# для запуска timeit или cProfile раскомментируй соответствующие строки
#
# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2
# Примечание по профилированию кода: для получения достоверных результатов при замере времени необходимо
# исключить/заменить функции print() и input() в анализируемом коде.
# С ними вы будете замерять время вывода данных в терминал и время,
# потраченное пользователем, на ввод данных, а не быстродействие самого алгоритма.
import cProfile
import timeit
# Eratosthenes
# n - порядковый номер искомого простого числа
# n = int(input('ввдеите порядковый номер простого числа: '))


def eratosthenes(n):
    sieve = [0]
    i = 2
    k = 0

    while (k + 1) <= n:

        for j in sieve[1:]:

            if i % j == 0:
                i += 1
                break
        else:
            sieve.append(i)
            k = sieve.index(sieve[-1])

    return sieve[-1]

cProfile.run('eratosthenes(20000)')

# s = eratosthenes(100000)
# print(f'for {n} counts the prime is {s}')
# print(timeit.timeit('eratosthenes(100000)', globals=globals(), number=1))
# print(eratosthenes(100000))
# -------------
# data from timeit

# 1.864999999999853e-05 with n=10 prime is 29
# 0.0007041279999999983 with n=100 prime is 541
# 0.06636302599999999 with n=1000 prime is 7919
# 11.231616412000001 with n=10000 prime is 104729
# 51.272770845000004 with n=20000 prime is 224737
# 116.730839471 with n=30000 prime is 350377
# 211.31011031500003 with n=40000 prime is 479909
# 351.15615848699997 with n=50000 prime is 611953
# 484.099713801 with n=60000 prime is 746773
# 676.577693966 with n=70000 prime is 882377
# 878.2507586739999 with n=80000 prime is 1020379
# 1114.671458194 with n=90000 prime is 1159523
# 1396.962016442 with n=100000 prime is 1299709

# data from cProfile
# n = 1000
#          2004 function calls in 0.066 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.066    0.066 <string>:1(<module>)
#         1    0.061    0.061    0.066    0.066 L4_t2_1.py:29(eratosthenes)
#         1    0.000    0.000    0.066    0.066 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1000    0.005    0.000    0.005    0.000 {method 'index' of 'list' objects}
#
# n = 10000
#          20004 function calls in 11.241 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   11.241   11.241 <string>:1(<module>)
#         1   10.751   10.751   11.240   11.240 L4_t2_1.py:29(eratosthenes)
#         1    0.000    0.000   11.241   11.241 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     10000    0.488    0.000    0.488    0.000 {method 'index' of 'list' objects}
#
# n = 20000
#          40004 function calls in 50.171 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   50.171   50.171 <string>:1(<module>)
#         1   48.200   48.200   50.171   50.171 L4_t2_1.py:29(eratosthenes)
#         1    0.000    0.000   50.171   50.171 {built-in method builtins.exec}
#     20000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     20000    1.968    0.000    1.968    0.000 {method 'index' of 'list' objects}

# данные по замерам производительности между timeit и cProfile - сходятся.



