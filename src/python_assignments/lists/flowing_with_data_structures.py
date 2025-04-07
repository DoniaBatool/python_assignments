def Add_data(my_list,data):
  
     print("list before is :",my_list)
     for i in range(3):
          my_list.append(data)

def Final():
     user_data=input("Enter the data: ")
     my_list=[]
     Add_data(my_list,user_data)
     print("The list after is :",my_list)
Final()