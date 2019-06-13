prompt = "\nType something, I will repeat it:"
prompt += "\nEnter quit to end."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)