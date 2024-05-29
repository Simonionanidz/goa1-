def friend(names):
   
    friend_names = [name for name in names if len(name) == 4]
    return friend_names


print(friend(["Ryan", "Kieran", "Jason", "Yous"]))  
print(friend(["Ryan", "Kieran", "Mark"]))           
