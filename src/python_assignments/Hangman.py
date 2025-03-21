import random

# Hangman words list
hangman_words = [
    "apple", "chair", "table", "ocean", "happy", "winter", "monkey", "house", "pizza", "garden",
    "mountain", "rainbow", "library", "seahorse", "balloon", "elephant", "sandbox", "festival", "jewelry", "dolphin",
    "watermelon", "hippopotamus", "astronaut", "chocolate", "adventure", "crocodile", "butterfly", 
    "landscape", "nightingale", "lighthouse"
]

# Hangman ASCII stages
Hangman_pics = [
    r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

print("Welcome to Hangman!")

game_over = False

while not game_over:
    start_quit = input("\nPress Enter to play or 'q' to quit: ").strip().lower()

    if start_quit == 'q':
        print("Exiting.....")
        game_over = True

    elif start_quit == "":
        word = random.choice(hangman_words)  # Random word select
        display = ["-" for _ in word]  # Hidden word initialize
        guessed_letters = []  # Track guessed letters
        lives = 6  # Total lives
        
        print("\nYou have 7 lives in total.")
        print(" ".join(display))  # Hidden word print

        while lives > 0 and "-" in display:  # Jab tak game chal raha hai
            guessed_letter = input("\nEnter a letter: ").lower().strip()

            if len(guessed_letter) != 1 or not guessed_letter.isalpha():
                print("Invalid input! Please enter only one letter.")
                continue

            if guessed_letter in guessed_letters:
                print(f"You have already guessed '{guessed_letter}'. Try another letter.")
                continue

            guessed_letters.append(guessed_letter)  # Guessed letter track karo

            if guessed_letter in word:  # Agar letter sahi hai
                for i in range(len(word)):
                    if word[i] == guessed_letter:
                        display[i] = guessed_letter
                print("Good guess!")
            else:  # Agar letter galat hai
                lives -= 1
                print("Wrong guess!")
                print(Hangman_pics[6 - lives])  # Hangman ka update dikhaye
                print(f"You have {lives} lives remaining.")

            print(" ".join(display))  # Updated word dikhaye

        if "-" not in display:
            print("\n🎉 Congratulations! You guessed the word correctly! 🎉")
        else:
            print(f"\nGame over! The word was '{word}'. Better luck next time!")

    else:
        print("Invalid input. Please try again.")

        



