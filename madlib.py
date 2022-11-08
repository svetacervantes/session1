f = open('madlibtest.txt', 'w')
f.write('The quick,\n')
f.write('*adjective\n')
f.write('*noun\n')
f.write('*past-tense verb\n')
f.write('over the lazy\n')
f.write('*noun\n')
f.write('.')
f.close()
f = open('madlibtest.txt', 'r')
story = ''
for line in f:
    if line.startswith('*'):
        text = input('Give me a(n) ' + line[1:].strip() + ': ')
    else:
        text = line

    story = story + ' ' + text.strip()

print("here's your story\n")
print(story)

f.close()



f = open('madlibstory.txt', 'w')
f.write(story)
f.close()