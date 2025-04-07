def User_elem():
    my_list=[]
    Over=False
    while not Over:
        user_input=input("Enter an element or press enter to stop: ")
        if user_input=="":
            print("The final list is :",my_list)
            Over=True
            
        else:
            my_list.append(user_input)
            print(my_list)
   
   
User_elem()