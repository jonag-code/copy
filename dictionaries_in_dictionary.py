#p.114 PCC by E. Matthes

users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton'}, 
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris'}  
		}
#Here they values of the key-value pairs are themselves dictionaries



for username, user_info in users.items():
	print("Username: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull Name: %s" % full_name.title() )
	print("\tLocation: %s \n" % location.title() )
