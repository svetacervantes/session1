filename=input('What are my thoughts?')
if'.' not in filename:
    filename=filename + '.txt'
f=open(filename, 'w')
f.write('I need to create a class for my tasks\n ')
f.write('I need to create a class for by board and include\n ')
f.write('To do, in progress and done\n')
f.close()
