import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def add_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

if __name__ == '__main__':
    n = int(sys.argv[1])
    primes = add_primes(n)
    print(*primes)
