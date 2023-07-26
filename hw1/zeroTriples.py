def find_triples(lst):
    triples = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == 0:
                    triples.append((lst[i], lst[j], lst[k]))
    return triples

def main():
    numbers = []
    number = int(input(""))
    while number != -12345:
        numbers.append(number)
        number = int(input(""))

    triples = find_triples(numbers)
    if triples:
        print(f"{len(triples)} triples found:")
        for triple in triples:
            print(", ".join(str(x) for x in triple))
    else:
        print("0 triples found.")

if __name__ == '__main__':
    main()
