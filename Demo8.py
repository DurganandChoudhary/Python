thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print()

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

print()

thistuple = ("apple", "banana", "cherry")
i=0
while i < len(thistuple):
  print(thistuple[i])
  i=i+1

print()

thistuple = ("apple", "banana", "cherry")
i=0
while i < len(thistuple):
  print(thistuple[i])
  i=i+1

print()

thistuple = ("apple", "banana", "cherry")
i=0
while i<len(thistuple):
  print(thistuple[i])
  i=i+1

print()


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print()

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print()

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

print()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

print()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(8)

print(x)

print()

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.

print()

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print()


thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


thisset = {"apple", "banana", "cherry"}

print(len(thisset))

print()

myset = {"apple", "banana", "cherry"}

print(type(myset))

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print()

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

print()

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

print()

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
print()

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print()


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

print()

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

print()

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

print()

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

print()

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set2.union(set1)
print(set3)

print()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print()

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

print()

#Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

print()

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

print()


x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

print()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

print()


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print()

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict) 


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)










































