#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

print()

x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

print()

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

print()

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

print()

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print()

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print()

a = "Hello, World!"
print(a[1])

print()

for x in "banana":
  print(x) 

print()

for x in "Kolkata":
  print(x)

print()

for x in "Patna":
  print(x)

for d in "Darbhanga":
    
    print(d)
print()

for c in "Chennai":
      print(c)

for v in "Vellore":
   print(v)

print()

for h in "Hyderabad":
   print(h)

print()

a = "Hello, World!"
print(len(a))
print()

ll="Mumbai"
print(len(ll))

print()

kk="Hello Everyone"
print(kk)

print()

#Check if "free" is present in the following text:

txt = "The best thing in life are free!"
print("free" in txt)

print()

txt2 = "Good morning everyone"
print("Good" in txt2)

print()

txt3 = "Life is Good when every thing is perfect"
print("imperfect" in txt3)
print("perfect" in txt3)

print()

#Print only if "free" is present:

txt = "The best thing in life are free !"
if "free" in txt:
   print("Yes, 'free' is present")

print()

txt4 = "The best thing in life are free !!"
if "best" in txt:
   print("Yes, 'best' is present")

   print()
   #Check if "expensive" is NOT present in the following text:

   txt5= "The best thing in Life are free!"
   print("expensive" not in txt)

print()

txt = "The best thing in life are free !"
if "expensive" not in txt:
   print("No, 'expensive' is NOT present")
   
print()

#SLICING

b = "Hello, World!"
print(b[2:5])

print()

c="hello everyone"
print(c[6:11])

print()

d="Good Morning Everyone"
print(d[2:7])

#Slice From the Start

b = "Hello, World!"
print(b[:5])

print()
#Slice To the End

b = "Hello, World!"
print(b[2:])

print()
#"""Negative Indexing
#Use negative indexes to start the slice from the end of the string:"""

b = "Hello, World!"
print(b[-5:-2])

print()

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World!     "
print(a.strip())
      
print()

a="Hello, World"
print(a.replace("H", "J"))

B= 'LUCKY BOYS'
print(B.replace("L", "m"))

print()

a = "Hello, World!"
b = a.split(",")
print(b)

print()

n="Hello Boys"
print(n.split(" "))

