# Condition SYNTAX :

# if condition == True:
#     do this
# else:
#     do that

# POINTS TO REMEMBER ABOUT CONDITIONS:
# starts with 'if' keyword
# describe the condition neccessary
# followed by a colon
# indentation on the right
# instruction followed by it for if statement



# Voter age Check
age = input("Input your age: ")

if int(age) >= 18:
    print('You are eligible for voting.')

else:
    print('You are not eligible for voting. Try again, after You turn 18.')


# Height Check for Roller Coaster

height = float(input("Input your height: "))

if float(height) <= 1:
    print("You cannot ride, under 1m")
elif float(height) == 3:
    print("Adults not allowed")
elif float(height) >=2:
    print("You cannot ride, over 3m")
else:
    print("You can ride")
    
    
          

