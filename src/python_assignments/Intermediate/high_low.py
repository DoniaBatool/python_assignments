import random
def Game():
    Rounds=1
    Score=0
    print("Welcome to the High-Low Game")
    print("You have five rounds in total to play this game")
    start_quit=(input("press enter to continue or press 'q' to quit the game:")).lower().strip()

    if start_quit=='q':
        print("Exiting....")
        return
    
    elif start_quit=="":
        while Rounds!=5:
                    comp_num=random.randint(1,100)
                    user_num=random.randint(1,100)
                    print("Round:",Rounds)
                    print("Your number is:",user_num)
                    
               
                    user_guess=input("What do you think? is your number high or low than computer number (h/l):")
                    if user_guess=="h" and user_num > comp_num:
                            print("Correct!Your number is higher than computer's")
                            Score+=1
                    elif user_guess=="h" and user_num < comp_num:
                            print("Wrong!Your number is lower than computer's")
                    elif user_guess=="l" and user_num < comp_num:
                            print("Correct!Your number is lower than computer's")
                            Score+=1
                    elif user_guess=="l" and user_num > comp_num:
                            print("Wrong!Your number is higher than computer's")
                    else:
                        print("Invalid Input,try Again!")
                        continue
                    Rounds+=1
                    if Rounds==5:
                        print("Rounds Completed,Your score is:",Score)
                        break
    else:
        print("Entered invalid input")
Game()