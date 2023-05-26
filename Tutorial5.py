############  Chained Conditionals  ################

# we have 3 chained contionals,which are as follows
# and, or, not


x = 2
y = 3
# "and" Conditional
if x == y and x + y == 5: #both of the conditions here needs to be true
    print(' :) ')
else:
    print(' :( ')
    
    
# "or" Conditional
if y == 3 and x + y == 5: #either one of the conditions here need to be true
    print(' :) ')
else:
    print(' :( ')


# "not" Conditional
if not(y == 3 and x + y == 5): #it changes the original value
    print(' :) ')
else:
    print(' :( ')



############  Nested If Statements   ################

x = 2
y = 3

#we can create as many nested if-else statements as required

if x == 2: #if statement
    if y == 3: #nested if statement
        print('x = 2, y = 3')
    else:
        print('x = 2, y != 3')#nested else statement
else:
    print(' x != 2')#else statement




