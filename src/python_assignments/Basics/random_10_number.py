import random
#first method

print("first mwethgod for printing 10 random numbers in the range of 1-100")
number_list=[]
for i in range(10):
    my_numbers=random.randint(1,100)
    number_list.append(my_numbers)
print(*number_list)


#second method
def main():
    print("Sdecond method for printing 10 random numbers in the range of 1-100")
    for i in range(10):
        my_numbers=random.randint(1,100)
        print(my_numbers,end=" ")


if __name__=="__main__":
    main()
