import random
jokes = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "What did one wall say to the other wall? I'll meet you at the corner!",
    "Why don’t eggs tell jokes? Because they might crack up!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call fake spaghetti? An impasta!"
]

user_input=input("Hi! I am a joke bot, how may I assist you? ")
def main():
        if (user_input).lower().strip()=="tell me a joke":
            joke=random.choice(jokes)
            print(joke)
        else:
            print("wrong prompt.I am a joke bot and i can tell jokes only,try giving the prompt 'tell me a joke'")
if __name__ == "__main__":
    main()