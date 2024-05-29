user_input = input("Enter a number: ")


try:
    number = float(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()


if number > 0:
    print("The entered number is positive.")
elif number < 0:
    print("The entered number is negative.")
else:
    print("The entered number is zero.")