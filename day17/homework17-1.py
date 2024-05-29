def sum_of_list(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum


numbers = [1, 2, 3, 4, 5]
print("Sum of numbers in the list:", sum_of_list(numbers))