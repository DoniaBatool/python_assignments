Sentence="I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to."
def Affirmation():
     user_input=input(f"Enter this statement correctly:\n{Sentence}\nTry out:")
     if user_input==Sentence:
          print("Bravo!You have typed it correctly.")
     else:
          print("OOPS!Check out there must be a mistake while typing the sentence")
Affirmation()