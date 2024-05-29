age = int(input("Enter your age: "))


if age < 0:
    print("Invalid age. Please enter a valid age.")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 65:
    print("Adult")
else:
    print("Senior Citizen")