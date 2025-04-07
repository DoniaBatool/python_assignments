def Func1(lst):
    Access=lst[0]
    print("The first Element in the  list is: ",Access)
     

def User_elem():
    my_list=[]
    Over=False
    while not Over:
        user_input=input("Enter element to create a list or press enter to stop: ")
        if user_input=="":
            Over=True
        else:
            my_list.append(user_input)
    
    Func1(my_list)
User_elem()

    