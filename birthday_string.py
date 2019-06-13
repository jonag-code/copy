age =  25
hbd = "Happy " + str(age) + "th Birthday!"
print(hbd)

#Without the "string converter" str() python doesn't know what to do 
#with the numerical variable, age.

message = "I'm currently " + str(age) + ". In a couple months\
 I will be " + str(age +1) + " years old."

print(message)