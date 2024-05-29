num = 1
sum_of_evens = 0


while num <= 10:
    
    if num % 2 == 0:
        
        sum_of_evens += num
    
    num += 1


print("The sum of even numbers from 1 to 10 is:", sum_of_evens)