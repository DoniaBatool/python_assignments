#string concatenation methods
youtuber:str="Donia Batool"

#method 1
print("Subscribe to "+youtuber)

#method 2
print(f"Subscribe to {youtuber}")

#method 3
print("Subscribe to {}".format(youtuber))

#method 4
print(("Subscribe to %s")%(youtuber))

#final example

adj:str=input("Enter the adjective:")
verb1:str=input("Enter a verb:")
verb2:str=input("Enter another verb:")
noun:str=input("Enter a noun:")

madlib:str=f"""My name is {noun}.I love {verb1}.
-Sometimes i also {verb2}.I am a {adj} person."""

print(madlib)