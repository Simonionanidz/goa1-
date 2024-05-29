correct_password = "Goa best"
incorrect_count = 0

while True:
    user_input = input("Please enter the password: ")
    if user_input == correct_password:
        print("Correct password entered!")
        break
    else:
        print("Incorrect password!")
        incorrect_count += 1

print("Number of incorrect attempts:", incorrect_count)