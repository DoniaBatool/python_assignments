'''fruit_list=['apple', 'banana', 'orange', 'grape', 'pineapple']

print(len(fruit_list))

fruit_list.append("mango")
print(f"fruit_list after appending 'mango' in to the list: {fruit_list}")




def Access():
    my_list=(input("Enter some fruits:")).split(",")
    length=len(my_list)
    print(f"This is the list of fruits you entered: {my_list}")
    fruit_name=input("Add your favourite fruit name to the list:")
    ind=int(input(f"Enter index number from 0-{length-1} at which you want your favourite fruit: "))
    if ind > length-1 or ind <0:
        print("Invalid index number entered")
        return
    my_list.insert(ind,fruit_name)
    print("This is your final list:",my_list)
Access()


num_list=[1,2,3,4,5]
def Modify(list,ind,new_val):
    try:
        print("This is a modify function")
        list[ind]=new_val
        print("The list has been modified:",num_list)
    except ValueError:
        print("Entered invalid numeric value")

Modify(num_list,2,110)


my_fruit=["apple","mango","banana","orange"]
def Slicer(my_list:list,start:int,end:int):
    try:
        print("This is Slicing the list function")
        Sliced=my_list[start:end]
        print("This is the sliced list:",Sliced)
    except IndexError:
        print("Invalid index number")
Slicer(my_fruit,1,3)'''


def Index_Game():
    
        print("Welcome to the INDEX GAME")
        operation=(input("Select the operation (Access, Modify, Slice, Quit): ")).lower().strip()
        if operation=="quit":
            print("Exiting....")
            return
        your_list=input("Enter five things to form a list (comma seperated):").split(",")
        length=len(your_list)
        if operation=="access":
            access_ind=int(input(f"Enter the index number to access the element from the list from 0-{length-1}"))
            Accessed=your_list[access_ind]  
            print("The element you requested to access is:",Accessed) 
        elif operation=="modify":
            modify_ind=int(input(f"Enter the index number to modify the element from the list from 0-{length-1}"))
            modification=input("Enter the word for modification: ")
            your_list[modify_ind]=modification
            print("The list after modification is:",your_list) 
        elif operation=="slice":
            start=int(input(f"Enter start index to slice from 0-{length-1}:"))
            end=int(input(f"Enter end index to slice  0-{length-1}:"))
            Sliced=your_list[start:end]
            print("This is your sliced list",Sliced)
        else:
            print("Invalid input")




Index_Game()