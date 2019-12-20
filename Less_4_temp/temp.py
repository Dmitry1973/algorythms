import timeit
# Eratosfen
# n = int(input('ввдеите до какого числа искать простыет числа: '))


def eratosfen(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):

        if sieve[i] != 0:
            j = i * 2

            while j < n:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    return result


# print(result)
s = eratosfen(1000)

print(timeit.timeit('eratosfen(1000)', globals=globals(), number=1))

# D:\python\algorythms\Less_4_temp>python -m timeit -n 100 -s "import temp" "temp.eratosfen(100)"
# 0.002149683999999999
# 100 loops, best of 5: 21.5 usec per loop
# n = 100, loops = 100

# D:\python\algorythms\Less_4_temp>python -m timeit -n 100 -s "import temp" "temp.eratosfen(1000)"
# 0.027436203000000006
# 100 loops, best of 5: 274 usec per loop
# n = 1000, loops =100

# D:\python\algorythms\Less_4_temp>python -m timeit -n 1000 -s "import temp" "temp.eratosfen(1000)"
# 0.275686998
# 1000 loops, best of 5: 272 usec per loop
# n=1000, loops = 1000




