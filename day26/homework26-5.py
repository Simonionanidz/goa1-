def manual_reduce(original_list):
    
    copied_list = []
    
    
    for item in original_list:
        
        copied_list.append(item)
    
    
    return copied_list

original_list = [1, 2, 3, 4, 5]
copied_list = manual_reduce(original_list)

print("Original List:", original_list)
print("Copied List:", copied_list)