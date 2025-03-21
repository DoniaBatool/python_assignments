def Grading_System():
    while True:
        try:
            print("Calculate Your Grade")
            marks=float(input("Enter the Marks:"))

            if marks>=90:
                Grade = "A+"
            elif marks>=80:
                Grade ="A"
            elif marks>=70:
                Grade ="B"
            elif marks>=60:
                Grade ="C"
            elif marks >=50:
                Grade="D"
            
            print(f"Your Marks are : {marks} and your Grade is:{Grade}")
            
            input_quit=(input("Enter 'q' to quit or press enter to continue"))
            if input_quit.lower()=="q":
                print("Exiting Grade calculator....")
                break
        except ValueError:
            print("Enter numeric value for marks or 'q' to quit")
        
Grading_System()