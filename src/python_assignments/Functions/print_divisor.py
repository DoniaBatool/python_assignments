def divisor(num: int):
    my_lst = []
    for i in range(1, num + 1):
        if num % i == 0:
            my_lst.append(i)
    return my_lst

def main():
    try:
        user_input = int(input("Enter an integer: "))
        call = divisor(user_input)
        print(f"The divisors of {user_input} are {call}")
    except ValueError as v:
        print(f"Invalid input: {v}")

if __name__ == "__main__":
    main()
