#The try block will generate an error, because x is not defined:

try:
    print(x)
except:
    print("An exception occured")

print()

###################

try:
    print(x)
except NameError:
    print("Variable x not defined")
except:
    print("Something else went wrong")

print()
#######################

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print()

##############################

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#######################

try:
    print("Hello")
except:
    print("something went wrong")
else:
    print("Nothing went wrong")

print()
####################
# ##The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print()

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")


print()

################

try:
    f=open("demofile.txt")
    try:
        f.write("Lorium Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening file")


###################

try:
    f=open("demofile.txt")
    try:
        f.write("Lorium Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")



######################

x=-1

if x<0:
    raise Exception("sorry no number below zero")

########################

x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

####################

x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

#####################

x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")

####################

x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed ")

#######################

x="hello"

if not type(x) is int:
    raise TypeError("only integers are allowed")

###################

x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

##############

x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")




