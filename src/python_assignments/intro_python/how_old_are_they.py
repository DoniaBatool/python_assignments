

def Riddle():
        my_dict={}
        my_dict["Anton"]=21
        my_dict["Beth"]=my_dict["Anton"]+6
        my_dict["Chen"]=my_dict["Beth"]+20
        my_dict["Drew"]=my_dict["Chen"]+my_dict["Anton"]
        my_dict["Ethan"]=my_dict['Chen']
            
        for person in my_dict:
            print(f"{person} is {my_dict[person]}")
Riddle()