############# GLOBAL V/s LOCAL Variables #############


### Global variables:

# Global variables are defined outside of any function and can be accessed from any part of the program.
# They have a global scope,
# meaning they are accessible throughout the entire program,
# including within functions.


###  Local variables:

# Local variables are defined within a function and can only be accessed within that function.
# They have a local scope,
# meaning they are limited to the block or function where they are defined.


# Example  
var = 9         # this is a Global Variale 
loop = True     # this is a Global Variale
newVar = 23     # this is a Gloabl Variable

def func(x):
    newVar = 7  # this is a Local Variale
    
    # Changing Global Variable Values
    global loop  # use "global" keyword followed by the variable name
    loop = 767687
    
    print(newVar) #**
    if x == 5:
        return newVar

# comparing 2 same variables in different function
def otherFunc():
    newVar = 5
    print(newVar)
    

### Accessing Local variables ###

#print(newVar) # gives error cuz "newVar" can be called within "func" function
otherFunc()
func(3)

### Accessing Global variables ###
print(loop)
print(var)
print(newVar)





