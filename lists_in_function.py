
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		completed_models.append(current_design)
		print("Printing model: " + current_design)
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
		


Unprinted_designs = ['dodecahedron','robot pendant','iphone case']
Completed_models = []

print_models(Unprinted_designs, Completed_models)
show_completed_models(Completed_models)
#USING Unprinted_designs[:] INSTEAD IN LINE 17 ENSURES THAT
#THE ORIGINAL LIST ISN'T MODIFIED. IT IS USUALLY BETTER
#TO ALLOW A FUNCTION TO MODIFY A LIST. COPYING LISTS IS VERY 
#COSTLY IN TERMS OF MEMORY AND COMPUTATION TIME.
#------------------------------------------------------------------
def build_profile(first,last,**user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
#this function creates a dictionary out of a list.	

user_profile = build_profile('albert',
							'einstein',
							location = 'princeton',
							field = 'physics')

print(user_profile)

#The '**' in the build_profile() function recognizes an aribtrary 
#number of key-value pairs as in lines 35 and 36 of the user_profile
#list. Recall a single '*' recognizes an arbitrary number of single 
#variable types, as in functions.py .