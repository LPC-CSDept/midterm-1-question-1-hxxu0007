

def main():
    all_even = 0
    number = []
    even_state = 1
    even_cnt = 0

    for i in range(10):
        number.append(int(input('Enter a number: ')))
            
    for i in range(10):
        if(number[i] % 2 == 0):
            all_even += 1
            if all_even >= 2 and even_state == 1:
                even_cnt += 1
                even_state = 0
        else:
            all_even = 0


    """
    ########################################
    Code Your Program here
    ########################################
    """
    print(even_cnt)

    ########################################
    # Do not delete the return statement
    ########################################
    return even_cnt


if __name__ == '__main__':
    main()
