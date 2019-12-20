import cProfile
import timeit
import sys


def f_simple_int():
    num = 2
    while 1:
        num += 1
        for i in range(2, num):
            if num % i == 0:
                break
            elif i == num - 1:
                yield num


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__itet__'):
      if hasattr(x, 'items'):
          for xx in x.items():
              show_size(xx, level +1)
      elif not isinstance(x, str):
          for xx in x:
              show_size(xx, level + 1)

# k = int(input('Введите число: '))

def primes(k):
    gen_sim_int = f_simple_int()
    for i in range(k - 1):
        prime_num = next(gen_sim_int)

    return prime_num

cProfile.run('primes(1000)')


show_size(cProfile)
show_size(f_simple_int())

# print((timeit.timeit('primes(40000)', globals=globals(), number=1)))

# -----------
# data from timeit
#
# 2.376000000000461e-05 with k=10
# 0.0023632739999999985 with k=100
# 0.405084795 with k=1000
# 80.288254248 with k=10000
# 371.11366810199996 with k=20000
# 897.4053246990001 with k=30000
# 1675.074507762 with k=40000
#
# ---------------
# data from cProfile
#
# k = 1000
#          2003 function calls in 0.394 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.394    0.394 <string>:1(<module>)
#         1    0.000    0.000    0.394    0.394 L4_t2_2.py:18(primes)
#      1000    0.394    0.000    0.394    0.000 L4_t2_2.py:5(f_simple_int)
#         1    0.000    0.000    0.394    0.394 {built-in method builtins.exec}
#       999    0.000    0.000    0.394    0.000 {built-in method builtins.next}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# k = 10000
#          20003 function calls in 81.603 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   81.603   81.603 <string>:1(<module>)
#         1    0.006    0.006   81.603   81.603 L4_t2_2.py:18(primes)
#     10000   81.589    0.008   81.589    0.008 L4_t2_2.py:5(f_simple_int)
#         1    0.000    0.000   81.603   81.603 {built-in method builtins.exec}
#      9999    0.008    0.000   81.597    0.008 {built-in method builtins.next}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

