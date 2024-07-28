def count_consecutive_even(numbers):
    """
    Counts the number of sequences of consecutive even numbers in a list.

    Args:
        numbers (list): List of integers.

    Returns:
        int: Number of sequences with at least 2 consecutive even numbers.
    """
    consecutive_count = 0
    current_count = 0

    for num in numbers:
        if num % 2 == 0:
            current_count += 1
            if current_count == 2:
                consecutive_count += 1
        else:
            current_count = 0

    return consecutive_count

# Example usage
my_numbers = [2, 4, 6, 8, 10, 12, 14, 15, 16, 18]
result = count_consecutive_even(my_numbers)
print(f"Number of sequences with at least 2 consecutive even numbers: {result}")