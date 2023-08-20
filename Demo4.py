#String Concatenation

a='hello'
b='world'
c=a+b
print(c)

print()

a="Hello"
b="World"
c=a+" "+b
print(c)

print()

#String Format

age=36
txt = "My Name is Python and I am {}"
print(txt.format(age))

print()

age=40
txt = "My name is Python2 and I am {}"
print(txt.format(age))

print()

quantity = 3
item_n0 = 567
price = 49.95

myorder = "I want {} pieces of item {} for {} rupees"
print(myorder.format(quantity,item_n0,price))

print()

quantity = 3
item_n0 = 564
price = 49.97
myorder2 = "I want to pay {2} rupees for {0} pieces of item {1}"
print(myorder2.format(quantity,item_n0,price))

print()

#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"vikings\" from the north."
print(txt)

print()

txt = 'It\'s alright'
print(txt)

print()

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

print()

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

print()
txt ="\123\456\789\101\121"
print(txt)

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)



txt = "python is FUN!"

x = txt.capitalize()

print (x)

txt = "banana"

x = txt.center(50)

print(x)

print()

txt = "Hello, welcome to my world."

x = txt.find("world")

print(x)

print(" \n")

txt = "50"

x = txt.zfill(19)

print(x)
print()

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

  print()

  s=100
  n=50

  if s>n:
    print("S is greater than n")
  else:
    print("s is not greater than n")
    
print()

print(bool("Hello"))
print(bool(1542))
print(bool("55"))
print(bool('A'))

print()

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print()

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

print()

class myclas():
  def len(self):
    return 0
  
  myobj = myclass()
  print(bool(myobj))

print()

def myFunction() :
  return True

print(myFunction())

print()

def yourfunc() :
  return False

print(yourfunc())

print()

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print()

def firstfunc():
  return True

if firstfunc():
  print("YES !")
else:
  print("NO !")


print()

x = 200
print(isinstance(x, int))

print()




