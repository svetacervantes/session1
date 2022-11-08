
cls = input("what is one important class for all high school student?")
classes = []
while cls.lower() !="done":
    classes.append(cls)
    cls = input("what is one important class for all high school student, or "done" to end? ")

for cls in classes:
    print(cls)