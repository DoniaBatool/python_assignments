Peturksbouipo = 16
Stanlau = 25 
Mayengua = 48

def Voting():
    Age=int(input("Enter your age: "))
    if Age==Peturksbouipo:
                    print(f"""You are eligible for voting in Peturksbouipo as the age limit for voting there is
        {Peturksbouipo}.You cannot vote in Stanlau as the age limit for voting there is {Stanlau} 
        and age limit for voting in Mayengua is {Mayengua}.
        """) 
    elif Age==Stanlau:
                 print(f"""You are eligible for voting in Stanlau as the age limit for voting there is
        {Stanlau}.You cannot vote in Peturksbouipo as the age limit for voting there is {Peturksbouipo} 
        and age limit for voting in Mayengua is {Mayengua}.
        """) 
    elif Age==Mayengua:
                  print(f"""You are eligible for voting in Mayengua as the age limit for voting there is
        {Mayengua}.You cannot vote in Stanlau as the age limit for voting there is {Stanlau} 
        and age limit for voting in Peturksbouipo is {Peturksbouipo}.
        """) 
    else:
        print("You are no eligible for voting")
Voting()