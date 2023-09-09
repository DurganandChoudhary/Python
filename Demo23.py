
import re

txt = "The rain in spain"
x=re.search("^The.*Spain$",txt)

if x:
    print("Yes! We have a match!")

else:
    print("No match")


#######
print()


import re

pattern = r"[A-Z]+hutan"
text = '''
India, officially the Republic of India (ISO: Bhārat Gaṇarājya),
[21] is a country in South Asia. It is the seventh-largest country
 by area; the most populous country as of June 2023;[22][23] and from
   the time of its independence in 1947, the world's most populous 
   democracy.[24][25][26] Bounded by the Indian Ocean on the south, the
     Arabian Sea on the southwest, and the Bay of Bengal on the 
     southeast, it shares land borders with Pakistan to the west;[j] 
     China, Nepal, and Bhutan to the Hhutan north; and Bangladesh and Myanmar to
       the east. In the Indian Ocean, India is in the vicinity of Sri
         Lanka and the Maldives; its Andaman and Nicobar Islands share
           a maritime border with Thailand, Myanmar, and Indonesia. 

'''

matches=re.finditer(pattern,text)
for match in matches:
    #print(type(match.span()))
    print(match.span()[0])
    print(text[match.span()[0]:match.span()[1]])



######################################

import re

a="charlie and the chocolate factory"
b="xyz.xyz@gmail.com"
c="hello"
d="xyz,yz,xyzz,xyyz,xxzzy,zyz,xxy"

match=re.search(r"^xyz",b)
#match=re.findall(r"^xyz",b)
print(match)

#########################
print()


x="Hello World"
y="Learning Python"
z="Getting Knowledge"

match=re.search(r"l",z)
print(match)


print()
###########################

import re

txt="The rain in Spain"
#match=re.findall("ai",txt)
match=re.findall(r"ai",txt)
#match=re.search(r"ai",txt)
print(match)


##############################

import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


















