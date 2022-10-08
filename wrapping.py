name=input("What is your name?:  ")
from random import randrange

x = randrange (10)
y = randrange (10)
op = randrange (5) # +, -, *, /, %

if op == 0:
    userans = input("what is" + str(x) + " + " + str(y) + "?"  )
    ans = x-y

userans = input("what is" + str(x) + " + " + str(y) + "?"  )
if int(userans) == x+y: 
    print("nice work")
else:
    print("sorry, the answer is " + str(x+y))
    