import sys

def factor_num(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 1:
        factors.append(int(n))
    if len(factors) == 0:
        factors.append(n)
    return factors

if __name__ == '__main__':
    n = int(sys.argv[1])
    factors = factor_num(n)
    print(*factors)
