
total_sum = 0


while True:
    user_input = input("Enter a number (or 'done' to finish): ")


    if user_input.lower() == 'done':
        break

    try:
       
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done' to finish.")


print("Sum of entered numbers:", total_sum)