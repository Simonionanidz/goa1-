
def find_short(s):
    
    words = s.split()
    
   
    word_lengths = [len(word) for word in words]
    
    
    return min(word_lengths)


print(find_short("bitcoin take over the world maybe who knows perhaps"))  
print(find_short("turns out random test cases are easier than writing out basic ones")) 