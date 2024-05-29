


correct_pin = "1234"


balance = 1000.0


user_pin = input("Enter your PIN: ")


if user_pin == correct_pin:
    print("PIN accepted. Welcome to the ATM!")

    while True:
        print("\nMenu:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")

        
        choice = input("Enter your choice (1-4): ")

        
        if choice == "1":
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            if withdrawal_amount <= balance:
                balance -= withdrawal_amount
                print(f"Withdrawal of ${withdrawal_amount:.2f} successful.")
            else:
                print("Insufficient funds for withdrawal.")
        elif choice == "2":
            deposit_amount = float(input("Enter deposit amount: "))
            balance += deposit_amount
            print(f"Deposit of ${deposit_amount:.2f} successful.")
        elif choice == "3":
            print(f"Current Balance: ${balance:.2f}")
        elif choice == "4":
            print("Exiting ATM. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
else:
    print("Incorrect PIN. Access denied.")