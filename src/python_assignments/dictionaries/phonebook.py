my_data={"donia":1234,
         "sosun":67575,
         "sidra":567456}

def my_phonebook(name:str,num:int):
    my_data[name]=num
    return my_data

def search(name:str):
    if name in my_data:
        return my_data[name]
        


def main():
    print("Welcome to the Phonebook!")
    user_input=int(input("Press 1 to store the contact, press 2 to search the contact and 3 to show all contacts: "))
    if user_input==1:
        while True:
            Name=(input("Enter the name or press enter to quit: ")).lower()
            if Name=="":
                print("Exiting...")
                break
            else:
                Number=int(input("Enter the number: "))
                continue
            call=my_phonebook(Name,Number)
            print(call)
    elif user_input==2:
        contact_name=(input("Enter the contact you want to search:")).lower()
        call2=search(contact_name)
        print(f"The contact number of {contact_name} is {call2}")
    elif user_input==3:
        print (f"Here is the list of all the contacts in the phonebook:")
        for item in my_data:
            final=my_data[item]
            print(f"{item}:{final}")
            
        
    else:
        print("Invalid input")
        return


if __name__=="__main__":
    main()
