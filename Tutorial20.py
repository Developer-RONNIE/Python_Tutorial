###  Classes & Objects ###

x = 'liz'
y = 23
z = True
a = 3.54

print(type(x)) #output: x is an object of string class
print(type(y)) #output: y is an object of int class
print(type(z)) #output: z is an object of bool class
print(type(a)) #output: a is an object of float class


#In simple language, an attribute refers to a characteristic or property that describes an object.
#It represents a piece of information associated with an object.
#For example, if we consider a car as an object,
#its attributes could include its color, brand, model, and year.
#Attributes provide specific details or qualities about an object and help define its state or characteristics.
#They can be accessed and modified to retrieve or update information related to the object.
# Attribute can be variables/ methods / etc...



# therefore, we cannot add x and y implicitly
# vm = x + y # output: Error
# print(y.count('1')) # output: Error
print(x.count('1')) # will run this code


#REMINDER : Functions & Methods are different things

#### Introduction to Classes ####
m = 'string'
n = 46


#Example 1:
class number():
    def __init__(self):
    #these are the methods inside of a class which looks similar to a function
        self.var = 46

    def display(self, m):
        print(m)


#* call our method 
n = number()        
n.display(21)
        



# Example 2 : with more than 1 parameter
class numbers():
    def __init__(self, num):
        self.var = num


    def display(self,m):
        print(m)

num = numbers(23)
print(num)
num.display(num.var)


