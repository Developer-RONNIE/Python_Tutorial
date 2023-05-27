######### LISTS #########

# List are data types
# denoted by square brackets []
# it is a collection of different datatypes
# everthing separeted by a comma can be defined as an item

#example
fruits = ['apple', 'pear', 3]
#this lists contains 2 string values and 1 integer value
print(fruits)


# INDEX/INDICIES
# every charcater/items has it's own position automatically defined my in a
# particular programming langugages
# Index value starts from '0'


# Finding out a particular item in a list
print(fruits[0]) #finding apple
print(fruits[1]) #finding pear
print(fruits[2]) #finding 3


# How to add an item to the list
#using '.append' command which means add at the end
fruits.append('pineapple')
print(fruits)

# Adding an item at the front/anywhere of the list:
fruits.insert(0, 'grapes')


# How to change an item to the list
fruits[1] = 'mango'
print(fruits)



######### TUPLES ######### 

# It is another Data type
# Tuples in Python are immutable ordered sequences of elements,
# typically used to store related pieces of data.
# They are like little treasure boxes
# where you can put different things together.
# Once you put something in a tuple, you can't change it.
# Tuples help us keep things organized and safe!

position = (2,3)
color = (255,255,255)
print(type(color))

