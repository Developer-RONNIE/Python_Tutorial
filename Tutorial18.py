##########3 TRY & EXCEPT ##########

# Error Handling & Exception Handling

#Uncomment the below code(Remove # from the below code to check it)

#Username = input("Enter Your Username: ")
#number = int(Username) # Suppose we want our username to be created by only numbers 
#print(number)


Username = input("Enter Your Username: ")
try:
    number = int("Your Username is: ",Username)
    print(number)
except:
    print('Invalid Username, Only Numbers Allowed')



