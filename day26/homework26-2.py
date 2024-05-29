def manual_max(lst):
    
    if not lst:
        return None  
    
    
    max_val = lst[0]  
    
    
    for num in lst[1:]:
       
        if num > max_val:
            max_val = num
    
   
    return max_val


print(manual_max([3, 1, 4, 1, 5, 9, 2, 6, 5]))  
print(manual_max([-10, -5, -8, -3]))           
print(manual_max([]))                           