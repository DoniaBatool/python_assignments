import random


def Game():
    print("Welcome to Guess the Number Game!")
    print("You have 5 attempts in total to guess the number.Best of luck!")
    while True:
        quit_start=(input("To start the game press enter or press 'q' to quit")).lower().strip()
        if quit_start == 'q':
                print("Exiting........")
                return
        elif quit_start == "":
            system_guess=random.randint(1,10) 
            total_attempts:int=5
            attempted:int=0 
            while attempted != total_attempts:
                try:
                    attempted +=1

                    user_guess=int(input("Guess the number between 1 and 10:"))
                
                    remaining_attempts = total_attempts-attempted

                    if user_guess > system_guess:
                        print(f"The number you have guessed is too high.You have {remaining_attempts} attempts remaining")
                    elif user_guess < system_guess:
                        print(f"The number you have guessed is too low.You have {remaining_attempts} attempts remaining")
                    else:
                        print(f"Congrats! You have guessed the correct number. The number is {system_guess} ")
                        break
                    if attempted == total_attempts:
                         print("You are out of attempts.Better luck next time!")
                except ValueError:
                        print("Invalid format or numeric values")
        else:
                print("invalid input")
            
  
Game()
    
        

   

   
            

        

       

        
            
        
  