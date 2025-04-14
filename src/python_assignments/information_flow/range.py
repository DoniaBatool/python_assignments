def in_range(n:int, low:int, high:int)->bool:
    
        if high>low>n:
            if low>=n<=high:
                return True
            else:
                return False
        else:
            return False
            print("The second number should be higher than the first number and lower than the third number")


def main():
    one=int(input("Enter the first number: "))
    two=int(input("Enter the second number: "))
    three=int(input("Enter the third number: "))
    call=in_range(one,two,three)
    print(call)


if __name__=="__main__":
    main()