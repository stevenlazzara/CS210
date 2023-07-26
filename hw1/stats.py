def main():
    numbers = read_input()
    if numbers:
        mean = sum(numbers) / len(numbers)
        numbers.sort()
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2 if len(numbers) % 2 == 0 else numbers[len(numbers)//2]
        stdev = (sum((x - mean) ** 2 for x in numbers) / len(numbers)) ** 0.5
        print("mean:", mean)
        print("median:", median)
        print("standard deviation:", stdev)
    else:
        print("No numbers were entered")

def read_input():
    numbers = []
    while True:
        n = int(input(""))
        if n == -12345:
            break
        numbers.append(n)
    return numbers


main()




