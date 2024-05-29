sum_of_numbers = 0


while True:
    user_input = input("Enter a number (or 'exit' to finish): ")


    if user_input.lower() == 'exit':
        break


    try:
        num = float(user_input)
        sum_of_numbers += num
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")


        print(f"The sum of the entered numbers is: {sum_of_numbers}")