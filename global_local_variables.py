spam = 42  ##Global variable within the Global scope

def eggs():
    spam = 42   ##Local variable within the local scope


print('Some code here')
print('Some code here')



##Variables can have the same name and same value provided one is a global variable
##i.e outside of any functions and one is a local variable within a functions code.


def spam():
    global eggs  ##This command allows a global variable to be set from inside a function (local  scope)
    eggs = 'Hello'
    print(eggs)
spam()
