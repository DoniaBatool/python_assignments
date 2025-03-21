

import random
def Guess():
        print("Guess the Number")
        print("I am guessing a number between 0-10")
        system_number=random.randint(0,10)
        user_guess=int(input("Enter the Number:"))
        while user_guess!=system_number:
            
            if user_guess>system_number:
                    print("Too high")
                    user_guess=int(input("Enter new Number:"))
            elif user_guess<system_number:
                    print("Too low")
                    user_guess=int(input("Enter new Number:"))
    
            
            
        if user_guess==system_number:
               print("You have guessed the number correctly.You win!")
        else:
                print("invalid input or numeric data")
Guess()