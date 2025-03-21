import random
import images



print("WELCOME TO ROCK PAPER SCISSOR GAME:")
while True:
    quitter=input("press 'q' to quit the game or press enter to continue:")
    if (quitter).lower().strip()=='q':
        print("Exiting......")
        break
    elif quitter == "":
        try:
            user_choice=int(input("press 0 for Rock, 1 for Paper, 2 for Scissors"))
            
            if user_choice < 0 or user_choice >= 3:

                print("You entered invalid number")
                continue
            elif user_choice>=0 and user_choice<=2:
                print("\n user chose:")
                print(images.images[user_choice])
                computer_choice=random.randint(0,2)
                print("Computer chose:")
                print(images.images[computer_choice])
                if user_choice == computer_choice:
                    print("Its a Draw!")
                elif user_choice == 0 and computer_choice == 2:
                    print("You win!")
                elif user_choice == 2 and computer_choice == 0:
                    print("You loose!")
                elif user_choice < computer_choice:
                    print("You win!")
                elif user_choice > computer_choice:
                    print("You loose!")
        except ValueError:
            print("invalid input or numeric value")
        

    else:
        print("You enterd invalid input")
        continue


