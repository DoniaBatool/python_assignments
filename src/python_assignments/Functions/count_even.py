def take_list():
    my_list = []
    even_list = []

    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":
            break  # Stop taking input when enter is pressed

        try:
            number = int(user_input)
            my_list.append(number)
        except ValueError:
            print("Please enter a valid integer or press enter to stop.")
            continue

    for num in my_list:
        if num % 2 == 0:
            even_list.append(num)

    print(f"The even numbers from the list of given integers are: {even_list}")

take_list()
