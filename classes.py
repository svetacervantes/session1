class Student:
   def __init__(self, name= "", ID=-1, birthdate= "1/1/2000"):
    self.name= name
    self.ID = ID
    self.birthdate = birthdate

    def study(self):
         print(self.name+" is studying")

    def do_homework(self, course):
        print(self.name + "is doing homework for their " + course + "course.")
    
    def ask_question(self):
        print("wait, what?" )

class Teacher:
    def __init__(self, name= "", subject=""):
        self.name= name 
        self.subject= subject
    
cs100a=[]
name = ""
while name.lower() != "done":
    name=input("what is the Student's name, or done to quit? ")
    if name.lower() != "done":
        stud = Student()
        stud.name = name
        stud.ID = int(input("\t" + name + "id number:  "))
        stud.birthdate = input("\t" + name + "birthday:  ")
        tname=input("who is "+ name+ " teacher?")
        subject=input("what subject does " + tname + " teach?")
        t=Teacher (tname,subject)
        stud.teacher=t
        stud.subject=t
        cs100a.append(stud)


for stud in cs100a:
    print("\t" + stud.name)
    print("\t" + str(stud.ID))
    print("\t" + stud.birthdate)
    print("\t" + stud.name +" is taught by " + stud.teacher.name)
    print("\t" + "The subject is " + stud.subject.subject)

