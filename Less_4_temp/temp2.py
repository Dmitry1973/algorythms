import timeit
# Eratosfen

# n = int(input('ввдеите до какого числа искать простыет числа: '))

s = """\
n = 100
sieve = [i for i in range(n)]
sieve[1] = 0

for i in range(2, n):

    if sieve[i] != 0:
        j = i * 2

        while j < n:
            sieve[j] = 0
            j += i

result = [i for i in sieve if i != 0]"""
# print(result)

print(timeit.timeit(s, number=1_000))