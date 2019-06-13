
#p.142 in PCC

def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician, "\n")
#--------------------------------------------------------------------

def Get_formatted_name(first_name, last_name, middle_name =''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = Get_formatted_name('james','hendrix','marshall')
Musician = Get_formatted_name('james','hendrix')
print(musician)
print(Musician)

#Get_formatted_name(a,b,c = '') has the flexibility to take two 
#or three input values as evidenced by lines 29 and 30.