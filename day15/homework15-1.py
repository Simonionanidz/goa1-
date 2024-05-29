def next_even(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is not even. The next even number is {num + 1}.")

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    next_even(user_input)