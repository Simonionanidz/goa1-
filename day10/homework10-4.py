
correct_pin = "1234"


balance = 1000


def atm_menu():
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")


def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ${balance}")
    else:
        print("Insufficient funds. Withdrawal failed.")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposit successful. New balance: ${balance}")


def check_balance():
    print(f"Your current balance is: ${balance}")


pin_attempt_count = 0
max_pin_attempts = 3

while pin_attempt_count < max_pin_attempts:
    
    user_pin = input("Enter your PIN: ")

   
    if user_pin == correct_pin:
        print("PIN accepted. Welcome to the ATM!")
        
       
        while True:
            atm_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == "1":  
                amount = float(input("Enter the withdrawal amount: $"))
                withdraw(amount)
            elif choice == "2":  
                amount = float(input("Enter the deposit amount: $"))
                deposit(amount)
            elif choice == "3": 
                check_balance()
            elif choice == "4":  
                print("Thank you for using the ATM. Have a nice day!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
    else:
        print("Incorrect PIN. Please try again.")
        pin_attempt_count += 1

print("Too many incorrect PIN attempts. Your card is now blocked. Contact customer support.")