banned_users = ['andrew','carolina', 'marie','david']
user = 'david'


if user.lower() not in banned_users:
	print(user.title()+" you're not banned, say hello.\n")
else:
	print(user.title() + " you're banned.\n")


#OR in the style of C++:
size = len(banned_users) 
for n in range(0,size):
	if user.lower() == banned_users[n]:# and n < size:
		print(user.title() + " you're banned.\n")
		#print(n)
		break
	elif n == size -1:
		print(user.title()+" you're not banned, say hello.\n")
		#print(n)










	




