#create class

class myclass:
    x=5
    
print(myclass)

#########################

# create object

class myclass:
    x=5
p1=myclass()
print(p1.x)

######################

class MyClass:
    x=5
p1=MyClass()
print(p1.x)

##############

class MyClass:
    x=10
p1=MyClass()
print(p1.x)


#######################

class MyClass():
    x=99

p1=MyClass()
print(p1.x)

############################

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#######################
print()
####################

class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age

p1=Person("Rahul", 36)
print(p1.name)
print(p1.age)

print()
########################

class Person:
   def __init__(self,name , age):
      self.name=name
      self.age=age

p1=Person("Aman",25)
print(p1.name)
print(p1.age)

print()
##################
      
class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age

p1=Person("Aman" , 36)
p2=Person("Rahul",65)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


print()
######################
# #The string representation of an object WITHOUT the __str__() function:

class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age

p1=Person("Rabi",55)
print(p1)

print()

#The string representation of an object WITH the __str__() function:

#The __str__() function controls what should be returned when the class object is represented as a string.

class Person():
   def __init__(self,name,age):
      self.name=name
      self.age=age
    
   def __str__(self):
      return f"{self.name}({self.age})"

p1=Person("Rahul" , 20)
print(p1)

print()

######################

class Person():
   def __init__(self,name,age):
      self.name=name
      self.age=age
    
   def __str__(self):
      return f"{self.name}({self.age})"
   
p1=Person("Aman" , 25)
print(p1)
      
print()
###########################

class Person():
   def __init__(self,name,age):
      self.name=name
      self.age=age

   def __str__(self):
      return f"{self.name}({self.age})"

p1=Person("Ravi" , 45)
print(p1)

########################
print()
#####################

class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age
    
   def myfunc(self):
      print("Hello my name is " + self.name)

p1=Person("DELL", 42)
p1.myfunc()

print()
########################

class Person():
   def __init__(self,name,age):
      self.name=name
      self.age=age

   def myfunc(self):
      print("Hello my name is " + self.name)

p1=Person("Aman" , 30)
p1.myfunc()

############################
print()



class Person:
   def __init__(mysillyobject,name,age):
      mysillyobject.name=name
      mysillyobject.age=age

   def myfunc(abc):
      print("Hello my name is " + abc.name)

p1=Person("Bikash" , 56)
p1.myfunc()

      
print()
########################

class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age

   def myfunc(self):
      print("Hello my name is " + self.name)

p1=Person("John" ,60)
p1.age=40
print(p1.age)


print()
###########################


class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement









































































