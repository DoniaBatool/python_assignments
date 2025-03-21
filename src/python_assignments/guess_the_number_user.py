import random

def computer_guess_game():
    print("Welcome to the Computer Guess the Number Game!")
    print("Think of a number between 1 and 10, and the computer will try to guess it.")
    input("Press Enter when you're ready...")

    low = 1
    high = 10
    attempts = 5
    computer_attempts = 0

    while computer_attempts < attempts:
        computer_attempts += 1
        guess = (low + high) // 2  # Binary search approach (middle value)

        print(f"Computer guesses: {guess}")
        user_feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower().strip()

        if user_feedback == "c":
            print(f"Computer guessed the correct number {guess} in {computer_attempts} attempts!")
            return
        elif user_feedback == "h":
            high = guess - 1
        elif user_feedback == "l":
            low = guess + 1
        else:
            print("Invalid input! Please enter 'h' for high, 'l' for low, or 'c' for correct.")
            computer_attempts -= 1  # Don't count invalid attempts

        if low > high:
            print("Something went wrong! Did you change your number? 😅")
            return

    print("Computer ran out of attempts! You win!")

computer_guess_game()
