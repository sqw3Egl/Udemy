# for loops iterate a specific number of times unlike while loops that can be inifinite 'while' True.

print('My name is ')
for i in range(5):
    print('Jimmy Five Times.' + str(i))

# variable i is set to 0 at the start

total = 0
for num in range (101):
    total = total + num
print(total)

# while loop equivilent

print('My name is')
i = 0
while i < 5:
    print('Jimmy five Times' + str(i))
    i = i + 1
    
#break and continue can be used in for loops
#range() function can have (1, 10) or (1, 10, 2)
