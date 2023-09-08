#A variable is only available from inside the region it is created. This is called scope.


x = 300

def myfunc():
  print(x)

myfunc()

print(x)

print()
######################


#Function Inside Function


def myfunc():
  x=300
  def myinnerfunc():
    print(x)
    
  myinnerfunc()

myfunc()

print()
#####################

def myfunc():
  x=900

  def myinnerfunc():
    print(x)

  myinnerfunc()

myfunc()

print()

##################

#Global Scope

x = 300  #global variable

def myfunc():
  print(x)

myfunc()

print(x)


print()
##################
# 
# 
# #  Naming Variables

x=300

def myfunc():
  x=200
  print(x)

myfunc()

print(x)

print()

######################
# 
# 
# 
# #  Global Keyword

def myfunc():
  global x
  x=600

myfunc()

print(x)

#############################
print()
#####################


x=800

def myfunc():
  global x
  x=777

myfunc()

print(x)



















