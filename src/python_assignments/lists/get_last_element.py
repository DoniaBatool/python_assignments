def Func1(lst):
    Access=lst.pop()
    print("The last Element in the  list is: ",Access)
     
def Func2(lst):
    if lst:
        Access=lst[-1]
        print("The last Element in the  list is: ",Access)
    else:
        print("The list is empty")

def User_elem():
    my_list=[]
    Over=False
    while not Over:
        user_input=input("Enter element to create a list or press enter to stop: ")
        if user_input=="":
            Over=True
        else:
            my_list.append(user_input)
    
    Func2(my_list)
User_elem()
