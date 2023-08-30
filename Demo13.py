def myfunc():
    print("Hello from function")
myfunc()

################

def myfunc(fname):
    print(fname+ " Refsnes")

myfunc("Email")
myfunc("Tobias")
myfunc("Linus")

print()
###################

def myfunc(lname):
    print("Refsnes "+lname)

myfunc("Email")
myfunc("Tobias")
myfunc("Linus")

print()
######################

def myfunc(fname, lname):
    print(fname +" "+lname)

myfunc("Rahul", "Kumar")
myfunc("Aman", "Kumar")

print()

########################

def myfunc(*kids):
    print("The youngest child is " + kids[2])

myfunc("Email", "Tobias", "Linus")


##################################
print()

def myfunc(child3, child2 , child1):
    print("The youngest child is " + child3)

myfunc(child1="email", child2="tobias",child3="linus")


###################
print()
#################

def myfunc(child1,child2,child3):
    print("The youngest child is " + child3)

myfunc(child1 = "email", child2 = "tobias" , child3 ="linuss")

print()

######################
# #If the number of keyword arguments is unknown, add a double ** before the parameter name:

def myfunc(**kids):  
    print("His last name is " + kids["lname"])

myfunc(fname = "Tobias" , lname="Refsnes") 

print()
########################

def myfunc(**kid):
    print("His last name is "+ kid["lname"])

myfunc(fname = "tobias" , lname= "refenses")


############################
print()

def myfunc(country = "Norway"):
    print("I am from " + country)
myfunc("Sweden")
myfunc("India")
myfunc("Brazil")
myfunc()
myfunc("Poland")

print()

def myfunc(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

myfunc(fruits)

print()

#######################

def myfunc(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]        

myfunc(fruits)


print()
###########################

def myfunc(x):
    return 5*x

print(myfunc(3))
print(myfunc(5))
print(myfunc(9))


print()
##############


def myfunc(x):
    return 5*x

print(myfunc(9))
print(myfunc(4))
print(myfunc(7))

print()
#######################


def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement


def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    
    else:
        result=0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
    

print()
#################

def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    
    else:
        result=0
    return result
print("\n\nRecursion result example: ")
tri_recursion(9)
    
print()
#############################

def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    
    else:
        result=0
    return result

print("\n\nRecursion Example")
tri_recursion(6)

##################
print()

def tri_recursion(n):
    if(n>0):
     result = n+tri_recursion(n-1)
     print(result)

    else:
        result=0
    return result
tri_recursion(4)


print()

######################

def tri_recursion(n):
    if(n>0):
        result=n+tri_recursion(n-1)
        print(result)
    
    else:
        result=0
    return result

print("\n\nRecursion Example")
tri_recursion(8)


print()
#########################





















































