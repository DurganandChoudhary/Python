thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))


thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

#

mytuple = ("apple", "banana", "cherry")

print(type(mytuple))

#

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#

#for last item

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#

print()

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

print()

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

print()

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print()

x = ("apple", "banana", "cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)
print()

thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.append("orange")
thistuple=tuple(y)
print(thistuple)

print()

thistuple = ("apple", "banana", "cherry")
y=("orange",)
thistuple += y
print(thistuple)

print()


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

print()

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)

print()

#unpacking

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print()

#Using Asterisk*
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print()

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.Example


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print()























































































































































































