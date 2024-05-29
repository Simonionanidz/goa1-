num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))


start_num = min(num1, num2)
end_num = max(num1, num2)


for num in range(start_num, end_num + 1):
 
    if num % 5 == 0:
        print(num)