#def promptWord(startswith):
def promptWord(startsWith):
    word = input("give me a word that start with" + startsWith + ':')
    word.startswith("c")
    while word.startswith(startsWith)==False:
        print(word + 'does not start with ' + startsWith)
        word=input("give me a word that start with "+ startsWith + ':')

    return word
word = promptWord('c')
print("the winning word is" + word)