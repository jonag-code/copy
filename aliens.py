alien_0 = {'colour':'green', 'points':5} 
print(alien_0, "\n")
#This class is called a "dictionary".
#Elements of a dictionary come in "key-value" pairs
#Can start with an empty: alien_0 = {}

points_gained = alien_0['points'] 
#Stores the value ('5') of a key ('points') into a variable.
print("You shot the alien! +" +str(points_gained) + " points. \n")

del alien_0['points']
#deletes a key-value pair if it exists, otherwise error.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['colour'] = 'yellow'
alien_0['x-speed']='medium'
#If the keys dont exist (line 11 and 12) then
#this adds to the dictionary. Otherwise it 
#overwrites the entry (line 13 and 14).
print(alien_0, "\n")


print("Old x-position: " + str(alien_0['x_position']) )
if alien_0['x-speed'] == 'slow':
	x_incr = 1
elif alien_0['x-speed'] == 'medium':
	x_incr = 2
else: #fast alien
	x_incr = 3
alien_0['x_position'] += x_incr
print("New x-position: " + str(alien_0['x_position']) + "\n" )
#This simplified example updates the x-position of the
#alien based on it's x-speed given after 1 second, say.
print(alien_0)
