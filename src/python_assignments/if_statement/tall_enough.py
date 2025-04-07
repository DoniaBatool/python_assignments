def Rider():
    Eligible=50
    user_height=int(input("Enter your height: "))
    if user_height>=Eligible:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride!")
Rider()