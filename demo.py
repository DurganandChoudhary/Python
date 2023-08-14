print("Hello World !!!")

x = 5
y = "Hello, World!"

print(x)
print(y)


#This is a comment
#written in
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#Legal Variable Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#MANY VALUES TO MULTIPLE VARIABLE
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ['apple','banana','cherry','mango','grapes']
a,b,c,d,e = fruits

print(a)
print(b)
print(c)
print(d)
print(e)

k = "Python is awesome"
print(k)

x='python'
y='is'
z='awsome'
print(x,y,z)

X='PYTHON'
Y='IS'
Z='AWSOME'
print(X+Y+Z)

x = 5
y = "John"
print(x, y)

x="awsome"
def myfunc():
    print("Python is "+x)
myfunc()

#Create a variable inside a function, with the same name as the global variable
x="awsome"
def myfunc():
    x="Fantastic"
    print("Python is "+x)

myfunc()
print("Python is "+x)


def myfunc():
    global n
    n="FANTASTIC"

myfunc()

print("Python is "+ n)

u='awsome'

def myfunc():
    global i
    i='Fantastic'

myfunc()
print("Python is "+i)


    