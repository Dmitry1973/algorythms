import math
import timeit

def atkin(nmax):
    """
    Returns a list of prime numbers below the number "nmax"
    """
    is_prime = dict([(i, False) for i in range(5, nmax+1)])
    for x in range(1, int(math.sqrt(nmax))+1):
        for y in range(1, int(math.sqrt(nmax))+1):
            n = 4*x**2 + y**2
            if (n <= nmax) and ((n % 12 == 1) or (n % 12 == 5)):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 + y**2
            if (n <= nmax) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if (x > y) and (n <= nmax) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]
    for n in range(5, int(math.sqrt(nmax))+1):
        if is_prime[n]:
            ik = 1
            while (ik * n**2 <= nmax):
                is_prime[ik * n**2] = False
                ik += 1
    primes = []
    for i in range(nmax + 1):
        if i in [0, 1, 4]: pass
        elif i in [2,3] or is_prime[i]: primes.append(i)
        else: pass
    return primes

def get_primes(n):
    k = 0
    sieve = [2]
    j = 0
    if n == 0:
        return sieve[0]
    else:
        while j < n:
            sieve.append(atkin(k))
            k += 1
            del sieve[:-1]
            j = len(sieve[-1])
        return sieve[-1][-1]


print(get_primes(0))
