#def hello():
#    print('Howdy!')
#    print('Howdy!!!')
 #   print('Alright mate')

#hello()
#hello()
#hello()

#ABOVE: defines a new function called 'hello' which prints 3 greetings.
#this function is then called 3 times.


##BELOW: same as above but this time passing arguments into the function.

def hello(name):       ## 'name' is the parameter
    print('Hello ' + name)

hello('Alice')         ## 'Alice' is an argument that 'name'
                        ##the argument is assigned to the parameter
                        ##i.e name=Alice
hello('Bob')


