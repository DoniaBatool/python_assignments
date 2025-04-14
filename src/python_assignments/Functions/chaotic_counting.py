import random

DONE_LIKELIHOOD = 0.3  # 30% chance to stop

# This is the "done" function to randomly decide whether to stop
def done():
    return random.random() < DONE_LIKELIHOOD

# This is the function you have to complete
def chaotic_counting():
    for i in range(1, 11):  # Counting from 1 to 10
        if done():
            return  # Stop counting if done() returns True
        print(i, end=' ')  # Print number on the same line

# Main function
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")  # This will print after chaotic_counting ends

# Call the main function to run everything
main()

    
