def repeater(msg:str,repeat:int):
    for i in range(repeat):
        print(msg) 

def main():
    while True:
        try:
            msg=input("Enter the message:")
            if msg=="":
                print("empty message!")
                continue  
            repeat=int(input("Enter how many times you want to print the message: "))
            call=repeater(msg,repeat)
            return call
        except ValueError as v:
            print(f"Invalid input:{v}")

        except Exception as e:
            print(f"unknown error : {e}")
    

if __name__=="__main__":
    main()