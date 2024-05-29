def manual_min(lst):
    
    if not lst:
        return None  
    
    
    min_val = lst[0] 
    
   
    for num in lst[1:]:
        
        if num < min_val:
            min_val = num
    
    
    return min_val


print(manual_min([3, 1, 4, 1, 5, 9, 2, 6, 5]))  
print(manual_min([-10, -5, -8, -3]))           
print(manual_min([]))                           