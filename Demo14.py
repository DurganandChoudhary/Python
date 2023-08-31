
x=lambda a,b:a*b
print(x(5,8))


x=lambda a,b:a*b
print(x(9,7))


########################


x=lambda a,b,c,d,e : a+b+c+d+e
print(x(5,6,7,8,9))

def myfunc(n):
    return lambda a:a*n

mydoubler = myfunc(2)

print(mydoubler(11))


print()

#######################


def myfunc(n):
    return lambda a:a*n

mydoubler = myfunc(2)

print(mydoubler(111))

####################
print()


def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(4)
print(mydoubler(44))

print()
#######################

def myfunc(n):
    return lambda a : a*n

mydoubler=myfunc(4)
mytripler=myfunc(5)

print(mydoubler(2))
print(mytripler(6))


print()

#################################

###########
# #ARRAYA

cars = ["Ford", "Volvo", "BMW"]

print(cars)


####################

cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

########################

cars = ["Ford", "Volvo", "BMW"]
cars.pop(2)

print(cars)

###############################

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

print()
#########################

cars = ["Ford", "Volvo", "BMW"]
cars.sort()
print(cars)

###############################

cars = ["Ford", "Volvo", "BMW"]
cars.sort(reverse=True)
print(cars)

#################################


fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)





