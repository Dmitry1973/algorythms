

# n = int(input("n="))

def primes(n):
    lst = [2]
    k = 3

    while len(lst) < n:
        for i in range(3, k+1, 2):
            if (i > 10) and (i % 10 == 5):
                continue
            for j in lst:
                if j*j-1 > i:
                    lst.append(i)
                    k += 1
                    lst = list(set(lst))
                    break
                if i % j == 0:
                    break
            else:
                lst.append(i)

    return sorted(lst)

print(primes(10))
print(len(primes(10)))
