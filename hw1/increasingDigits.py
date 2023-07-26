import sys

def is_increasing(number):
    str_number = str(number)
    if len(str_number) == 1:
        return True
    if str_number[0] >= str_number[1]:
        return False
    return is_increasing(int(str_number[1:]))

def count_increasing_numbers(n, current=1):
    if current > n:
        return 0
    count = 1 if is_increasing(current) else 0
    return count + count_increasing_numbers(n, current + 1)

if __name__ == '__main__':
    n = int(sys.argv[1])
    result = count_increasing_numbers(n)
    print(result)