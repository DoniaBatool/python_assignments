Mercury= 37.6

Venus=88.9

Mars= 37.8

Jupiter=236.0

Saturn=108.1

Uranus=81.5

Neptune=114.0

def Weight():
    print("CHECK YOUR BODY WEIGHT ON DIFFERENT PLANETS")
    weight_on_earth=float(input("Enter your weight on Earth:"))
    planet_name=(input("Enter the planet name:")).capitalize().strip()
    if planet_name=="Mercury":
        answer=(Mercury/100)*weight_on_earth
    elif planet_name=="Venus":
        answer=(Venus/100)*weight_on_earth
    elif planet_name=="Mars":
        answer=(Mars/100)*weight_on_earth
    elif planet_name=="Jupiter":
        answer=(Jupiter/100)*weight_on_earth
    elif planet_name=="Saturn":
        answer=(Saturn/100)*weight_on_earth
    elif planet_name=="Uranus":
        answer=(Uranus/100)*weight_on_earth
    elif planet_name=="Neptune":
        answer=(Neptune/100)*weight_on_earth
    elif planet_name=="Earth":
        answer=weight_on_earth
    else:
        print("invalid input")
    print(f"Your weight on {planet_name} will be:",round(answer,2),"kg")
Weight()