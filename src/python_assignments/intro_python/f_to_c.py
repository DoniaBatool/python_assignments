def Temp():
    fahrenheit=float(input("Enter the temperature in Fahrenheit: "))
    degrees_celsius = (fahrenheit - 32) * 5.0/9.0
    rounded=round(degrees_celsius,2)
    print(f"The temperature in Celsius is: {rounded} C")
Temp()