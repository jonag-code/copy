

ALIENS = []
#create an empty list (to store dictionaries soon!)
#new_alien = {'colour':'green', 'points': 5, 'speed':'slow'}

for i in range(10):
	new_alien = {'colour':'green', 'points': 5, 'speed':'slow'}
	ALIENS.append(new_alien)
print("Number of aliens created: " + str(len(ALIENS)) +'\n')
print(ALIENS, "\n")


for alien in ALIENS[0:3]:
	if alien['colour'] == 'green':
		alien['colour'] = 'yellow' 
		alien['speed'] = 'medium' 
		alien['points'] = 10
#for alien in ALIENS[0:5]: print(alien)


# better line 7
alien_0 = {'colour':'yellow', 'points': 5, 'speed':'slow'}
aliens = [alien_0 for x in range(10)]
print(aliens)










