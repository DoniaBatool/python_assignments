my_dict = {
    "apple": 20,
    "mango": 30,
    "orange": 30,
    "banana": 20
}

def calculate_cost(fruit, amount):
    if fruit in my_dict:
        cost = amount * my_dict[fruit]
        return cost
    else:
        return None

def main():
    while True:
        user_input = input("Enter the fruit you want to buy (or press enter to quit): ")
        if user_input == "":
            print("Thank you for visiting!")
            break

        if user_input not in my_dict:
            print("Sorry, that fruit is not available.")
            continue

        try:
            amount = int(input(f"How many {user_input}s would you like to buy? "))
            total_cost = calculate_cost(user_input, amount)
            print(f"Your total bill for {amount} {user_input}(s) is: ${total_cost}")
        except ValueError:
            print("Please enter a valid number for amount.")

if __name__ == "__main__":
    main()
