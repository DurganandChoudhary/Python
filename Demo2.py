x='awsome'
def myfunc():
    print("Python is "+x)
myfunc()

y='fantastic'

def myFunc():
    global y
    print(y)
myfunc()
print(y)

n='good'
def myfunc():
    global n
    n='very good'
    print("Hi "+n)
myfunc()
print(n)

x=5
print(type(x))

x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 



x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 
print()

x = bytearray(5)

#display x:
print(x)
print()
#display the data type of x:
print(type(x))

print()

x=str("Hello World !!!")
print(x)
print()
print(type(x))

print()
#Python Numbers

x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

print()

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print()

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print(


)

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

print()

print()

import random
print(random.randrange(1,10))

print(random.randint(1,9))
print(random.seed(1,5))
print()

print(random.getstate())

print()

import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)

print()

mylist=["cabbage","grapes","mango"]
random.shuffle(mylist)
print(mylist)

print()
import random
print(random.uniform(30,90))
print()

print(random.triangular(20,60,30))

print()

import random

x = random.getstate()

print(x)

print()
import random

#print a random number:
print(random.random())

#capture the state:
state = random.getstate()

#print another random number:
print(random.random())

#restore the state:
random.setstate(state)

#and the next random number should be the same as when you captured the state:
print(random.random())

print()
print()

import random

#print a random number
print(random.random())
#capture the state
state=random.getstate()
#print another random number
print(random.random())
#restore the state
random.setstate(state)

#print the next random number should be the same as when you captured the state
print(random.random())



