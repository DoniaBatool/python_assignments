def input_digit(num:int):
    number=str(num)
    unit=number[-1]
    print(f"The digit at the unit place in the given number is: {unit}")



def main():
    my_num=int(input("Enter the number to find out its one(th) digit: "))
    call=input_digit(my_num)
    return call

if __name__=="__main__":
    main()