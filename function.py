#function----it is a resuable block of code
#1.local scope- it defined within a function.
'''def my_function():
    x=10
    print(x)
my_function()

def my_function():
    x=10
    y=5
    print(x+y)
my_function()'''

#global scope--it defined outside the function
'''y=20
def my_function():
    print(y)
my_function()'''

# non-local scope- modify a global variable from wihin a function 
x=10
def modify_global():
    global x
    x=20
    print(x)
modify_global()
