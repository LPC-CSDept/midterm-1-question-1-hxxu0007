def bubble(number):
    """Swap all two adjacent values if left one is greater than the right one."""
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            number[i], number[i + 1] = number[i + 1], number[i]
    return number

def bubblesort(number):
    """Call bubble(number) N times, N is the length of number."""
    for _ in range(len(number)):
        number = bubble(number)
    return number

lst = [35, 5, 10, 20, 40, 15]
sorted_lst = bubblesort(lst)
print(sorted_lst)

