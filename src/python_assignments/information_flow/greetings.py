#Required output
"""What's your name? Sophia

Greetings Sophia!"""

def greet(name:str):
    print(f"Greetings {name}!")


def main():
    user_input=input("Enter your good name:")
    call=greet(user_input)
    return call


if __name__=="__main__":
    main()