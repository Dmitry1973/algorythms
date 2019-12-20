import timeit
# # Version_1
# n = int(input('введите целое число '))    # число, до которого хотим найти простые числа


# n = 29
# numbers = list(range(2, n + 1))
# for number in numbers:
#     if number != 0:
#         for candidate in range(2 * number, n+1, number):
#             print(candidate)
#             numbers[candidate-2] = 0
# primes = list(filter(lambda x: x != 0, numbers))
# print(primes)
# # print(*list(filter(lambda x: x != 0, numbers)))    # выводим простые числа
# print(primes.index(primes[-1]) + 1)
# print(primes[-1])


def get_prime(n):
    numbers = [2]

    while numbers.index(numbers[-1]) + 1 <= n:
        for number in numbers:
            if number != 0:
                for candidate in range(2 * number, n+1, number):
                    numbers[candidate-2] = 0


    primes = list(filter(lambda x: x != 0, numbers))

    return primes[-1]

print(get_prime(100))