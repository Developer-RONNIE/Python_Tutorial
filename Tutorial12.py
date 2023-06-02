############### Function ###############

# A function in Python is a reusable block of code that performs a specific task.
# It can be called multiple times and accepts input parameters to customize its behavior.


# Syntax :
#def function(parameter):
#    return statement

#function() This is also called as call statement
#print() this is also called as print statement

##################


# Easy Example usage:
def add(x):
    return x + 2
addition = add(70)
print(addition)

def sub(y):
    return y -2
substraction = sub(20)
print(substraction)



def liz(love):
    return love*10000
Ronnie = liz(10000)
print(Ronnie)



def printString(string):
    print(string)
printString("Hello ")
printString("My name is Ron")



def accel(mass, force): # multiple parameters
    a = mass * force
    return a
print(accel(2,5))



def lost(): # no parameter
    print ("Hii")
print(lost())


# Complex Example usage:

# Creating bodmas function hard way
# Brackets: Perform operations inside brackets first.
# Orders: Evaluate exponential (power) operations next.
# Division: Perform division operations from left to right.
# Multiplication: Perform multiplication operations from left to right.
# Addition: Perform addition operations from left to right.
# Subtraction: Perform subtraction operations from left to right
def bodmas(z):
    return 3 + 4 * (z - 1) / 5 ** 2

result = bodmas(3)
print(result)

# Creating bodmas function simple way
def bodmas(expression):
    return eval(expression)
result = bodmas("3 + 4 * (3 - 1) / 5 ** 2")
print(result)


# Creating a Greeting Function for new Employee
def Greeting(employee_name, employee_post):
    message = print("Hello," + employee_name + "! Welcome to the company. Congrats as joining us as the " + employee_post)
    return message

employee_name = input("Enter employee Name : ")
employee_post = input("Enter employee Post : ")

Greeting(employee_name, employee_post)





