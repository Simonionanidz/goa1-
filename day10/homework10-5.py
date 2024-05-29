correct_username = "admin"
correct_password = "password123"


user_username = input("Enter your username: ")
user_password = input("Enter your password: ")


if user_username == correct_username and user_password == correct_password:
    print("Login successful")
else:
    print("Login failed. Incorrect username or password.")