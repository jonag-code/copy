#p.112 PCC by E. Matthes


favourite_languages ={'jen':['python','ruby'],'sarah':['c'],'phil':['python','haskell'], 'edward':['ruby','go']  }

for NAME, LANGUAGES in favourite_languages.items():
	print("%s's favourite languages are: " %NAME.title())
	for language in LANGUAGES:
		print("\t" + language.title())
#Note: skipping the second for loop and trying to print would end
#up printing the entire list of languages for a given person.


#--------------------------------------------------------------------------------
#I wouldn't know how to do something similar in C++ with the 
#equivalent data type "library". Without the items() function
#I would have to do convert the key-value pairs into seperate lists?





