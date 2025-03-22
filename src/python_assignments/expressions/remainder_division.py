def main():
    first_num=int(input("Enter first number: "))
    second_num=int(input("Enter second number: "))
    division=round((first_num/second_num),2)
    remainder=first_num%second_num
    print(f"The result of division is {division} and their remainder is {remainder}")

if __name__=="__main__":
    main()