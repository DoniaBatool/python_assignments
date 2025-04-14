
def make_sentence(word:str,part_of_speech:int):
    if part_of_speech==0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech==1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech==2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("invalid input(s)")
    



def main():
    my_word=input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    my_num = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    call=make_sentence(my_word,my_num)
    return call



if __name__ == "__main__":
    main()