magicians = ['alice','david','carolina']

for x in magicians: 
	print (x.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, "+x.title()+".\n")
print("Thank you everyone. That was a great show!")
# this loop begins with the first entry of the list magicians,
# stores the entry into variable x
#prints message containing x
# loops to the next, overwriting x, until finished the list.
#Indented messaged printed at the end/ doesn't get looped.

#Extra: In C++ one would have to not only define x ahead of time, but
#also identify the type of variable (int x vs char x....yuck..). In 
#addition one would need to use brackets to organize what's in/ out
#of a for loop. Here the indents do the work. 