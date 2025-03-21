



def double():
    user_entered=int(input("Enter a number to double it until its 100 or greater than 100:"))
   
    while user_entered<=100:
         user_entered=user_entered*2
         print(user_entered ,end=" ")


double()