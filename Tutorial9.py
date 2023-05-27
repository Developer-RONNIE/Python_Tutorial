#########  Advanced For Loops  ########

#using for loop in a list
# Iterating by Index
fruits = ['apples', 'pears', 'bananas', 'pineapples']

for fruit in fruits:
    print(fruit)


    

### Difference Iterating by Index  V/s  Iterating by Items ###
    
######## Iterating by Index:  ########
# 1. When iterating by index, you use numbers to go through each item
# in a sequence (like a list or string).
# It's like counting from the beginning to the end and
# checking each item along the way.
# 2. You can easily access and modify items by their positions in the sequence,
# like opening different doors in a row to see what's inside.
# 3. It's helpful when you need to know the exact position of an item or
# when you want to change specific items based on their indexes.

########  Iterating by Items:  ######## 
# 1. When iterating by items,
# you look at each item directly without worrying about their positions.
# It's like looking at things one by one without any numbers.
# 2. You can use the items themselves to perform actions or make decisions,
# like looking at fruits and deciding which ones you like
# without caring about their order.
# 3. It's useful when you only care about the values and not their positions,
# or when you want to perform operations
# based on the items themselves rather than their indexes.


# Iterating by Items
for fruit in fruits :
    if fruit =='pears':
        print(fruit)
    else:
        print('Not pears')


# Iterating by Index
for fruit in range(0, 4): # or using (len(fruits))
    if fruits[fruit] == 'pears':
        print(fruits[fruit])
    else:
        print('not pears')
        
