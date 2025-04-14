
my_lst=[]

def get_user_numbers(num:int):
    my_lst.append(num)
    return my_lst
    
def my_dict(lst):
    my_data={}
    for num in lst:
        if num in lst:
            counter=lst.count(num)
            final=f"{num} appears {counter} times"
            result=my_data[num]=final
            print(result)


def main():
   
    while True:
        user_input=input("Enter the number or press enter to quit: ")
        if user_input=="":
            print("The reult is:")
            break
        else:
            convert=int(user_input)
            call1=get_user_numbers(convert)
            print (call1)
            continue
    call2=my_dict(my_lst)
    
if __name__=="__main__":
    main()