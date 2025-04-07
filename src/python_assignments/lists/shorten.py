def Func1(lst):
    while len(lst):
        popped_item=lst.pop()
        print("The removed item is: ",popped_item)
     

def Func2():
    my_list=["rat","bat","mat","cat","hat"]
    Func1(my_list)
Func2()