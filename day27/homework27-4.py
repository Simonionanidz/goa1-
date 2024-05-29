def getMiddle(word):
    
    length = len(word)
    
    
    middle_index = length // 2
    
    
    if length % 2 != 0:
        
        return word[middle_index]
    else:
        
        return word[middle_index - 1: middle_index + 1]


print(getMiddle("test"))    
print(getMiddle("testing"))  
print(getMiddle("middle"))  
print(getMiddle("A"))        