

def main():
    number = []
    evencnt = 0

    for i in range(10):
        number.append(int(input('Enter a number: ')))
        if(not number[i].isalpha()):
            print("The input value is not right.")
        if(number[i] % 2 == 0):
            evencnt += 1

    """
    ########################################
    Code Your Program here
    ########################################
    """
    print(evencnt)

    ########################################
    # Do not delete the return statement
    ########################################
    return evencnt


if __name__ == '__main__':
    main()
