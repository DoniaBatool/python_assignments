ADULT:int=18

def adult_age(num:int):
    if num>=ADULT:
        return True
    else:
        return False


def main():
   while True:
        input_age=(input("Enter the age of the adult or press enter to quit: "))
        if input_age=="":
            print("Exiting....")
            break
        else:
            given_age=int(input_age)
            call=adult_age(given_age)
            print(call)
            continue 
        

if __name__=="__main__":
    main()