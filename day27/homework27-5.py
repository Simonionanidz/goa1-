def high_and_low(numbers):
    
    numbers_list = [int(num) for num in numbers.split()]
    
    
    max_num = max(numbers_list)
    min_num = min(numbers_list)
    
    
    return f"{max_num} {min_num}"


print(high_and_low("1 2 3 4 5"))  
print(high_and_low("1 2 -3 4 5"))  
print(high_and_low("1 9 3 4 -5"))  