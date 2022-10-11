from random import randrange


userwins = 0
computerwins = 0
while userwins + computerwins < 7:
    while True:
        s = input("rock, paper, scisors:  ")

        computer = randrange(3)

        if computer == 0 and s == 'paper':
            print("you win ")
            userwins += 1
            break
        elif computer == 0 and s == 'scisors':
            print("I win")
            computerwins += 1
            break
        elif computer == 0 and s == 'rock':
            print("we tied")
            continue
        elif computer == 1 and s == 'scisors' :
            print("I win")
            computerwins += 1
            break
        elif computer == 1 and s == 'rock':
            print ("you win")
            userwins += 1
            break
        elif computer == 1 and s == 'paper':
            print ("we tie")
            continue
        elif computer == 2 and s == 'rock':
            print ("I win")
            computerwins += 1
            break
        elif computer == 2 and s == "paper":
            print ("you win")
            userwins += 1
            break
        elif computer == 2 and s == "scisors":
            print ("we tie")
            continue
