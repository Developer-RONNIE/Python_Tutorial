# .find(), .count()


string = 'Hello'

print(string.find('l')) # finding indicies of the letter 
# REMINDER: in programming indicies start with 0
print(string.find('H'))
print(string.find('o'))
print(string.find('7')) # output -1


print(string.find('l')) # counts number of letters present
print(string.find('A')) # output 0


# Real life Exapmle
# Suppose we don't want the user to use underscores(_) in there password

string = input("Please Type Password: ")
if string.count('_') > 0:  # it will count the number of _ 
    print('Not valid Password!')
else:
    print('Valid Password')
    

