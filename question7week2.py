def countnumeric(text):
    number = 0
    for c in text:
        if c.isnumeric():
            number = number + int(c)
    return number 
text = input ("phrase: ")
ncount=countnumeric(text)
print(str(ncount) + " numeric characters")