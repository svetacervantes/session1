from random import randrange
s = input("heads or tails, call it in the air:  ")

coin = randrange(2)

if coin == 0 and s == 'heads':
    print("you won the coin toss")
elif coin == 1 and s == 'tails':
    print("you won the coin toss")
else:
    print("I won the con toss")

print("Let;s start the game!")