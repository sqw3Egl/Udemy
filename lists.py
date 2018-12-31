#lists: lists are ALWAYS in [].

spam = ['cat', 'bat', 'rat', 'elephant']

print(spam)
print(spam[0])  ##variable spam value 0 in the list order(cat)
print(spam[3])  ##variable spam value 3 in the list order(elephant)
print(spam[2] + spam[1])

eggs = [['cat', 'bat'], [10, 20, 30, 40, 50]] ##multiple lists assigned to eggs variable.

print(eggs[0][0]) #prints from list position 0, integer 0 (i.e cat)
print(eggs[1][3]) #prints from list position 1, integer 3 (i.e 40)

#can print from the list in reverse order by using -ve index..(i.e 40)
print(eggs[1][-2])

#a slice takes multiple values from the list. This evaluates to a new list value.
#below takes values 0 to 3(but not including 3) and prints as a new list (in [] brackets)
print(eggs[1][0:3])

#an index can be used to assign a new vlaue to an existing  list.

eggs[1][3] = 70 ##changes 40 to 70
print(eggs[1][3])

#list function list() will return the string passed to it as a list

spamlist = list('Hello')
print(spamlist)
print(spamlist[2:4])


