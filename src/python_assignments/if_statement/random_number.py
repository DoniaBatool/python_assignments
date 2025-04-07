import random

def Random():
    print("These are your 10 random numbers from 1-100")
    for _ in range(10):
        random_numbers=random.randint(1,100)
        
        print(random_numbers,end=" ")
Random()
