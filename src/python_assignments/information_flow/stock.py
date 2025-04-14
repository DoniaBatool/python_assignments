def num_in_stock(fruit:str):
    my_lst=["apple","mango","orange","peach","apple","mango","mango"]
    
    if fruit in my_lst:
       counter=my_lst.count(fruit)
       print(f"There are {counter} {fruit}(s) in the inventory!")

    else:
       print(f"There are 0 {fruit}(s) in the inventory!")

def main():
  my_fruit=input("Enter the fruit:")
  call=num_in_stock(my_fruit)
  return call

if __name__=="__main__":
    main()
    