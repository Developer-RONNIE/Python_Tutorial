############## OPTIONAL PARAMETERS ############## 

#Reminder:
def func(x):
    print(x)

func(3)
func('Ron')

# when we have many parameters &
# we don't want to constantly rewrite the parameters
# we need to set default fault for our paramaters
# also we need to seet the other paramter or we can specify

# setting paramter 
def fun(y, text):
    print(y)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
fun('Liz', '2')

# default parameters (only one default parameter) 
def fun(y , text='1'):
    print(y)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
fun('Ron')
# Here 'text' is marked as optional parameter
# Since text parameter, it will take the default value of '1'
# However, if an argument is provided for text, it will override the default value


### Point to be Noted:
#in an optional parameter I can't specify default value to 'y',
#here in the example without assigning value to "text"
