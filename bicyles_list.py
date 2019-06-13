bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

bicycles[0] ='bmx' # Overwrites 1st term. Index starts at 0
del bicycles[-1]
print(bicycles) #-1 shortcut reference for last term

message = "My first bicycle was a " +bicycles[0].title() +"."
print(message ) 
