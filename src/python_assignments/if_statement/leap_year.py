def Leap():
    Year=int(input("Enter the year: "))
    if Year%4==0:
        if Year%100==0:
            if Year%400==0:
               print("That's a leap year!")
            else:
                print("That's not a leap year!")
        else:
            print("That's a leap year!")
    else:
            print("That's not a leap year!")
Leap()