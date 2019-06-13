my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] 
#copies list into another list from start to end entry

print("My fav foods:")
my_foods.append('canoli')
print(my_foods)

print("\nMy friend's fav foods are:")
friend_foods.append('ice cream') 
print(friend_foods)

#-------------------------------------------------------
#FOR DICTIONARIES YOU CANNOT USE APPEND. USE :

person = {'first': 'first_name', 'last': 'last_name'}
person['age'] = 'age'
print(person)