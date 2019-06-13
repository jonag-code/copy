favourite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}

for key, value in favourite_languages.items():
	print(key.title() + "'s favourite language is " + value.title() + "." )
	#print("%s's favourite language is %s." %(key.title(), value.title()) )
#The words "key" and "value" can be changed to be more descriptive, 
#such as "name" and "language". The "items()" function refers to the 
#pairs of a given dictionary. Lines 5 and 6 have same output.


if 'erin' not in favourite_languages.keys():
	print("\nErin, please take your poll!\n")



for x in favourite_languages.keys():
	print(x.title())
print("\n")
for y in favourite_languages.values():
	print(y.title())
print("\n")
#The "keys()" and "values()" functions refers to corresponding
#half of a key-value pair within a dictionary.



inters = set(['phil','sarah']).intersection(favourite_languages.keys())
for x in inters:
	print("Hey %s, I see your favourite language is %s!" 
	 	%(x.title(), favourite_languages[x].title()) )

#For clarity we can make the explicit lists:
		#friends = ['phil','sarah'] 
		#people = list( favourite_languages.keys() )
#and intersect these two into the third list "inters". If one prefers 
#not to creates unnecessary lists then the former approach is preferred.

