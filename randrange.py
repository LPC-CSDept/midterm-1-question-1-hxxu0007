import random

def main():
    numbers = [random.randrange(1,27,11) for i in range(9)]
    print(numbers)

main()