name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi there Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, granny')
    

#note that when this run all the if/elif statements are ignored that evaluate to False.
    #the only one that executes is the age > 2000 as this is True. 
