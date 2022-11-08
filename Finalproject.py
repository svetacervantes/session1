import os
import pickle


class Task:
    id = 0

    def __init__(self, description, status):
        # if task_id.txt exists, read the file into Task.id
        if os.path.isfile("task_id.txt"):
            id_file = open("task_id.txt", "r")
            Task.id = int(id_file.readline())

        self.description = description
        self.status = status
        self.id = Task.id

        Task.id += 1

        id_file = open("task_id.txt", "w")
        id_file.write(str(Task.id))

        # save Task.id to task_id.txt
    
    def __str__(self):
        return str(self.id) + " (" + self.status + "): " + self.description


class Board:
    def __init__(self):
        self.tasks = []
        self.load()

    def insert(self, task):
        self.tasks.append(task)

    def move(self, id, status):
        # 1. find task in self.tasks using the id
        # 2. set new status of task 
        task = next ((i for i in self.tasks if i.id == id), None)
        task.status = status

    def print(self):
        for task in self.tasks: print(task)

    def save(self):
        # use pickle to dump self.tasks into a file (tasks.dat)
        file = open("tasks.dat", "wb")
        pickledtask= pickle.dump(self.tasks, file)

    def load(self):
        # use pickle to load the file tasks.dat to self.tasks
        if os.path.isfile("tasks.dat"):
            file = open("tasks.dat", "rb")
            self.tasks = pickle.load(file)

        


board = Board()

# while true
# print board
# print message "what do u wanna do "
# get input
# if move
#   call move method
# board.save at the end of each loop
cmd = ''
while cmd != 'quit':
    board.print()

    cmd = input ("What do you want to do?, insert, move or quit: ")

    if cmd == "insert":
        description = input ("What task do you want to do?:  ")
        status = input ("What is the status of the task?:  ")

        task = Task(description, status)
        
        board.insert(task)

    elif cmd == "move":
        id = input("What is the id of the task:  ")
        status = input("What is the new status of the task?:  ")

        board.move(int(id), status)
    
        # get task id
        # get new status for task

        # board.move
        pass
    elif cmd != 'quit':
        print("invalid cmd")

    board.save()
