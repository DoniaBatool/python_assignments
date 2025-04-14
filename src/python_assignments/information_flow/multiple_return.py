def get_user_info(f_name:str,l_name:str,email:str):
    my_tuple=(f_name,l_name,email)
    return my_tuple
def main():
    first_name=input("Enter your First Name: ")
    last_name=input("Enter your Second Name: ")
    email=input("Enter your Email: ")
    call=get_user_info(first_name,last_name,email)
    print(f"The received data is : {call}")

if __name__=="__main__":
    main()