file = open('file1.txt', 'w')

file.write('python')
file.write('I am learning how to write in a file')

# suppose we want to break the senctence
# we simply add '\n' whihc is called 'back slash n' and the end of the sentence
# or where ever we want to break the sentence
file.write('\n')
file.write ('I am learning how to write in a file\n')
file.write ('Using Python\n')
file.write ('This is the 13th video \n of the python tutorial series')
file.close()
 
