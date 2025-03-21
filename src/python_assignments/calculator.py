print("My Calculator")
operators=['+','-','*','/']
while True:
    user_input=input("Enter the operator for the operation you want to perform (+,-,*,/) or press 'q' to quit:")
    if (user_input).lower().strip() == 'q':
        print("Exiting.....")
        break
    elif user_input in operators:
        first=(float(input("Enter First Number:")))
        second=(float(input("Enter Second Number:")))

        try:
            if user_input == '+':
                answer = first + second
            elif user_input == '-':
                if first > second:
                    answer = first - second
                else:
                    print("For subtraction first number should be greater than second number")
                    continue
            elif user_input == '*':
                answer = first * second
            elif user_input == '/':
                if second !=0:
                    answer = first / second
                else:
                    print("Division Error:cannot divide the number by zero")
                    continue
            print("Your answer is :", answer)
        except ValueError:
            print("Invalid operator or numeric value")
    else:
        print("Invalid input")
        