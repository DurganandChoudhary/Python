
class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)
    
x=Person("John" , "Doe")
x.printname()

##########################
print()
###################

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname , self.lname)

x=Person("Rahul" , "Kumar")
x.printname()

#####################
print()
##################

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
   
    def printname(self):
     print(self.firstname , self.lastname)

x=person("Aman", "Kumar")
x.printname()

#####################################
print()
####################################

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printnmae(self):
     print(self.firstname , self.lastname)

class Student(Person):
    pass

x=Student("Mike" , "Olsen")
x.printnmae()

#################
print()
#####################

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

x=Student("Raja" , "Ram")
x.printname()


###########################
print()
############################

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printnmae(self):
        print(self.firstname , self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x=Student("MS" , "Dhoni")
x.printnmae()

##################
print()
###############

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printnmae(self):
        print(self.firstname , self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
x=Student("Virat", "Kohli")
x.printnmae()

##############################
print()
#################

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname , self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x=Student("Rohit" , "Sharma")
x.printname()

###################
print()
####################

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x=Student("Vijay" , "Kumar")
x.printname()


#########
print()
##########

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname , self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
    
x=Student("Mike","Hussey")
x.printname()

###############
print()
###############

class Person:
    def __init__(self,fname,lname):
        self.irstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.lastname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x=Student("Narendra" , "Modi")
x.printname()


##############################
print()
###############  ADD PROPERTIES

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        self.graduationyear=2025

x=Student("Mohit","Kumar")
print(x.graduationyear)


#########################
print()
####################


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

x = Student( "Ajay","Jadeja",2025 )

print(x.graduationyear)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

######################
print()
######################

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to class of",self.graduationyear)

x=Student("Ravi","Kumar",2025)
x.welcome()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()


 

































