my_list=[]
def Even():
    for i in range(1,101):
        if i%2==0:
            my_list.append(i)
    
    Sliced=my_list[:20]
    print("Here are your twenty Even Numbers!")
    for num in Sliced:
        
        print(num,end=" ")
    
Even()
