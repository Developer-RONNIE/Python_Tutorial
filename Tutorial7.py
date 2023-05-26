###########  While Loop Syntax ###########  
# while condition == True:
#    do this
#    break


# While Loop is used when
# we are not sure how many times
# we need to iterate over the condition
# inorder to achieve our task done

# example - there are suppose X number of files in a database
# that needs to be deleted, We use while loop to finish our task
# so while loop will stop when our condition is fullfilled
# after iterating X number of times(i.e, unknown to


loop = True

while loop:
    text = input('Insert something: ')
    if name == 'stop':
        break


###########  Password Checker   ###########

import re

while True:
    password = input("Enter password: ")

    #Limiting/CHecking the length of the password
    if len(password)< 8: #len is the keyword to count length
        print("Password should be atleast 8 characters long.")
        continue
    
    #Check for atleast one capital letter
    if not re.search(r'[A-Z]', password):
        print("Password should contain at least one capital letter.")
        continue
    #Check for atleast one small letter
    if not re.search(r'[a-z]', password):
        print("Password should contain at least one small letter.")
        continue
    #Check for atleast one number
    if not re.search(r'\d', password):
        print("Password should contain at least one number.")
        continue
    #Check for atleast one special character
    if not re.search(r'[!@#$%^&*()\-=_+{};:,.<>?]', password):
        print("Password should contain at least one special character.")
        continue

    # If all conditions are met, break out of the loop
    break

print("Password is Valid.")
print(" Your password is ", password)
    
    
        





