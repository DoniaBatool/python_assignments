#There are 12 inches per foot. Foot is the singular, and feet is the plural.
inches_in_foot=12
def Converter():
    user_input=float(input("Enter the value of feet to convert it into inches: "))
    in_inches=user_input*inches_in_foot
    answer=round(in_inches,2)
    print(f"There are {answer} inches in {user_input} feet/foot")
Converter()