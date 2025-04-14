def subtract_seven(num:int):
    if num>=7:
        subtract=num-7
        print(f"The number after subtracting 7 is: {subtract}")
    else:
        print(f"Cannot subtract 7 from {num} as it is less than 7 ")
        
   
        
             

def main():
    while True:
        number=(input("Enter the number or press enter to quit: "))
        if number=="":
            print("Exiting...")
            break
        else:
            my_num=int(number)
            call=subtract_seven(my_num)
            return call
            continue
        
            
if __name__=="__main__":
    main()