# create an empty list
team = []

# ask the user for names.
# enter 'done' when complete
player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)

print('your team is: ')
team.reverse()
for p in team:
    print("\t" + p)
if "sveta in team" :
    print ("I can/'t wait to play")
else:
    print ("put me in coach, I/'m ready to play.")