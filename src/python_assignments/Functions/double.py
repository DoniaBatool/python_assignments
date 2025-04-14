def double(num_list):
    for num in num_list:
        final=num*2
        print(f"The double of {num} is {final}")

my_list = []

while True:
    user_input = input("Enter the number or press enter to stop: ")
    if user_input == "":
        break
    try:
        number = int(user_input)
        my_list.append(number)
    except ValueError:
        print("Invalid input! Please enter a number.")

double(my_list)
