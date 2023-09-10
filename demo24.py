
import re

txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")



print()

import re

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


print()

################################



import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


print()

import re

txt = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

##################################
print()



import re

txt="The rain in Spain"
match=re.findall("ai",txt)
print(match)

print()

####################


import re

txt="The rain in spain"

match=re.findall("Portugal",txt)

print(match)

if(match):
  print("yes there is atleast one match.")
else:
  print("no match")

print()


import re

txt="The rain in Spain"
match=re.search("\s",txt)
print("The first white space character is located in position:",match.start())

print()

import re

txt ="The rain in spain"
match=re.search("Portugal",txt)
print(match)

print()

import re

txt="The rain in Spain"
match=re.split("\s",txt)
print(match)

print()

####################


import re

txt="The rain in Spain"
match=re.split("\s",txt,1)
print(match)

print()

##################################


import re

txt="The rain in Spain"
match=re.sub("\s","9",txt)
print(match)

print()

######################


import re

txt="The rain in Spain"
match=re.sub("\s","9",txt,2)
print(match)

print()

############################

import re

txt="The rain in Spain"
match=re.search("ai",txt)
print(match)

print()

import re

txt="The rain in Spain"
match=re.search(r"\bS\w+",txt)
print(match.span())

print()
#########################

import re

txt="The rain in Spain"
match=re.search(r"\bS\w+",txt)
print(match.span())


print()

import re

txt="The rain in Spain"
match=re.search(r"\bS\w+",txt)
print(match.span())


##################

import re

txt="The rain in Spain"
match=re.search(r"\bS\w+",txt)
print(match.span())

############################


import re

txt="The rain in Spain"
match=re.search(r"\bS\w+",txt)
print(match.string)


#########################

import re

txt="The rain in Spain"
match=re.search(r"\bS\w+",txt)
print(match.group())


#PIP

import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))
























