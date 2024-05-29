def find_largest_number(numbers):
    if not numbers:  # Check if the list is empty
        return None  # If the list is empty, return None
    max_number = numbers[0]  # Initialize max_number with the first element of the list
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

# Example usage:
input_numbers = [10, 5, 20, 15, 8]
largest_number = find_largest_number(input_numbers)
print("The largest number in the list:", largest_number)
