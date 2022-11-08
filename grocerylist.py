f=open('groceries.txt', 'w')
item = ''
while item != 'done' :
    item = input('enter grocery item, or done to exit:  ')
    if item != 'done' :
        f.write(item + '\n')
item = input("What else do we need? Type 'done' to quit. ")
f.close()
print("now go to the grocery store")
f=open('groceries.txt', 'r')
receipt = []
for grocery in f:
    print("don't forget " + grocery.strip() + ".")
    # item = input('what did you put in your cart?')
    # cost = input("how much did it cost?")
    # qty = input("how many of " + item + ":")
    # receipt.append((item, float(cost), int(qty)))
    # if item in grocerylist:
    #     grocerylist.remove(item)
    # else:
    #     print('Lists are never set in stone ')
print("hope you brought your own bags")
total = 0.0
for lineitem in receipt:
    (item, cost, qty) = lineitem
    total = total + (cost*qty)
    print(str(qty) + "" + item + "@$" + str(cost) + "=" + str(cost*qty))
print("=========================================================")
print('"TOTAL:"$ + str(total)')
