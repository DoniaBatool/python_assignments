import random
letter_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number_list=['0', '1','2', '3', '4', '5', '6', '7', '8', '9']

symbol_list=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', "<", ">", ",", ".", "?", "/"]

print("Welcome to Password Generator!")
while True:
        try:
            quitting=((input("Enter 'q' to quit or press enter to continue")).lower().strip())


            if quitting == "q":
                  print("Exiting......")
                  break
            elif quitting == "":
                
                letters=int(input("How many letters would you like to have in your password? \n"))

                symbols=int(input("How many symbols would you like to have in your password? \n"))

                numbers=int(input("How many numbers would you like to have in your password? \n"))

                password=[]

                for i in range(1,letters+1):
                    char = random.choice(letter_list)
                    password += char

                for i in range(1,symbols+1):
                    char = random.choice(symbol_list)
                    password += char

                for i in range(1,numbers+1):
                    char = random.choice(number_list)
                    password += char


                random.shuffle(password)

                final_password=""

                for char in password:
                    final_password += char

                print("The password is : ", final_password)
            else:
                 print("Invalid Value entered, try again! ")
                 continue
        except ValueError:
             print("Enter numeric values ONLY")    
             
      
        

