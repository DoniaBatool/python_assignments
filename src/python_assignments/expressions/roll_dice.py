import random
my_list=[]

def Dice_Roller():
    print("Welcome to Dice Roller!")
    for _ in range(2):
       random_numbers = random.randint(1,6)
       my_list.append(random_numbers)
    
    dice1=my_list[0]
    dice2=my_list[1]
    sum=dice1+dice2
    print("Dice 1 :",dice1)
    print("Dice 2 :",dice2)
    print("The sum  of the values of both the dice is: ",sum)    
Dice_Roller()
