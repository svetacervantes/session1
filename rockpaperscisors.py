from random import randrange
user = 'yes'
while user.lower() == 'yes' or user.lower() == 'y':
    s = input("rock, paper, scisors:  ")

    computer = randrange(3)

    if computer == 0 and s == 'paper':
        print("you win ")
    elif computer == 0 and s == 'scisors':
        print("I win")
    elif computer == 0 and s == 'rock':
        print("we tied")
    elif computer == 1 and s == 'scisors' :
        print("I win")
    elif computer == 1 and s == 'rock':
        print ("you win")
    elif computer == 1 and s == 'paper':
        print ("we tie")
    elif computer == 2 and s == 'rock':
        print ("I win")
    elif computer == 2 and s == "paper":
        print ("you win")
    elif computer == 2 and s == "scisors":
        print ("we tie")
    user=input("want to play again?")
