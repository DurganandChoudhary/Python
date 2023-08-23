
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

    print()

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print()

thislist = ["apple", "banana", "cherry"]

i=0

while i < len(thislist):
    print(thislist[i])
    i=i+1

print()

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  print()

  thislist = ["apple", "banana", "cherry"]
  i=0
  while i<len(thislist):
      print(thislist[i])
      i=i+1


print()


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

print()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

print()
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

print()

newlist = [x for x in range(10) if x<5]
print(newlist)

print()

newlist=[x for x in range(20) if x<10]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
print()


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=['hello' for x in fruits]
print(newlist)
print()


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x!= "banana" else "grapes" for x in fruits]
print(newlist)

print()


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)

print()

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)
print(thislist)
print()

def myfunc(n):
    return abs(n-50)
thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

print()

def myfunc(n):
    return abs(n-50)      #sort close to 50

thislist = [100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)
print()


def myfunc(n):
    return abs(n-50)

newlist = [100,65,50,24,82]
newlist.sort(key=myfunc)
print(newlist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)
print(thislist)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 
print()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print()

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print()


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


print()

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)
print()

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
print()













