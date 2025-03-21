def Spaceship():
    print("This is a space ship lift off program method 1")
    for i in range(10,0,-1):
        print(i,end=" ")
    print("lift off!")
Spaceship()

def main():
    print("This is a space ship lift off program method 2")
    num_list=[1,2,3,4,5,6,7,8,9,10]
    num_list.reverse()
    slogan:str="lift off!"
    for number in num_list:
        print(number,end=" ")
    print(slogan)
if __name__=="__main__":
    main()
