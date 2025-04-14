

first=float(input("Enter first number: "))
second=float(input("Enter second number: "))


   
def average(a:float,b:float)->float:
   sum=a+b
   avg=sum/2
   return avg



Average=average(first,second)
print(f"The average of given numbers is: {Average}")
