

def check(num_list):
    for num in num_list:
        if num%2==0:
            print(f"{num} even")
        else:
            print(f"{num} odd")
def main():
    my_lst=[]
    while True:
        my_num=(input("Enter the number or press enter to stop: "))
        if my_num == "":
            break
        try:
            checked_num=int(my_num)
            my_lst.append(checked_num)
            

        except Exception as e:
            print(f"invalid input: {e}")
            continue
    check(my_lst)

if __name__ == "__main__":
    main()