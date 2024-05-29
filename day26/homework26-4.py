def manual_len(lst):
   
    count = 0
    
    for _ in lst:
        count += 1
    
    return count

print(manual_len([1, 2, 3, 4, 5]))  
print(manual_len([]))               
print(manual_len(["a", "b", "c"])) 