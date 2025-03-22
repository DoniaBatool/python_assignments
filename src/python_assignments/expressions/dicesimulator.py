import random
my_list=[]
Round=1

def Dice_Roller():
    global Round
    print("Round=",Round)
    Round=Round+1
    my_list.clear()
    for _ in range(2):
       random_numbers = random.randint(1,6)
       my_list.append(random_numbers)
    
    dice1=my_list[0]
    dice2=my_list[1]
    sum=dice1+dice2
    print("Dice 1 :",dice1)
    print("Dice 2 :",dice2)
    print("The sum  of the values of both the dices is: ",sum,"\n")    
    

def DiceSimulator():
    print("Welcome to Dice Roller!")
    Dice_Roller()
    Dice_Roller()
    Dice_Roller()
    
        
  

DiceSimulator()