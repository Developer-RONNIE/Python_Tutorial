# Slice Operator
fruits = ['apples', 'pear', 'strawberrys']
text = 'Hello I Like Python'

# printing 2nd item in a list
print(fruits[1])

# printing 2nd element in an item
print(text[1])
print(text[10])

#slice operator works for a range items or elements in a list
# SYNTAX  : print (text[start:stop:step]

print(text[6:12])
print(fruits[1:2])

print(fruits[:2]) #by default from the start
print(text[:12])

print(fruits[1:]) #by default to the end
print(text[6:])

print(text[::3]) #use of step
print(fruits[::2])

#use of them all
print(text[3:12:3])


#ADDING ITEM TO OUR LIST
fruits[0:0] = "o" #adding at the beginning of the list
print(fruits)
fruits[3:3] = "b"  #adding in between of the list
print(fruits)
fruits[5:5] = 'p'  #adding at the end of the list
print(fruits)
