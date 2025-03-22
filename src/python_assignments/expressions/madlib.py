def Sentence(adj,noun,verb):
    print(f"My name is {noun}, I like cooking and {verb}.I am a {adj} person.")

def Madlib():
    print("Welcome to MADLIBS")
    print("My name is __________, I like cooking and ________.I am a ________ person.")
    Adj=input("Enter an Adjective: ")
    Noun=input("Enter a Noun: ")
    Verb=input("Enter a Verb: ")
    Sentence(Adj,Noun,Verb)
Madlib()



