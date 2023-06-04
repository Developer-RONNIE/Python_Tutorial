### How to read from a file ###

file = open('file.txt', 'r') #r stands for read mode
# instead of 'r' we can also use 'w' for write mode or we can simply leave it empty ''
# but i both of those case our content in the file will be cleared

f = file.readlines()

print(f)
# when we print the text in the file we get "/n" which denotes sentence break


## inorder to remove the backslashes we use for loop, as shown below

## METHOD 1: using for loop
## Reminder: for loop uses iterating by item

newList = []
for line in f:
    newList.append(line[:-1])
    # -1 goes to the lastcharacter but doesn't include the last character
    
print(newList)

# this way we get can see the last letter of the item is deleted too
newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)



## METHOD 2 : using strip keyword
newList = []
for line in f:
    newList.append(line.strip())
print(newList)
