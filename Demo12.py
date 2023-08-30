i = 1
while i < 6:
  print(i)
  if (i == 4):
    break
  i += 1

#############
print()
#############


i=1
while i<6:
  print(i)
  if(i == 3):
    break
  i += 1

###################
print()

i=1
while i<7:
  print(i)
  if(i==5):
    break
  i += 1

##################
print()
####################

i=0
while i<6:
  i += 1
  if i==3:
    continue
  print(i)

# Note that number 3 is missing in the result


i=0
while i<8:
  i += 1
  if i==5:
   continue
  print(i)

#############
print()
###############

i=0
while i<9:
  i += 1
  if i==6:
    continue
  print(i)

############
print()
##########


i=1
while i<6:
  print(i)
  i += 1
else:
  print("i is n longer less than 6")

##################
print()
###############

i=1
while i<6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

###########
print()
###################

i=1
while i<9:
  print(i)
  i += 1
else:
  print("i is no longer less than 9")


print()


i=1
while i<7:
  print(i)
  i += 1
else:
  print("i is no longer than 7")

print()


i=1
while i<9:
  print(i)
  i += 1
else:
  print("i is no longer than 9")

############################
print()
######################


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#####################

for x in "BANANA":
  print(x)

#################

#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#############

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x=="banana":
    break
##################
print()
########################

fruits = ["apple", "banana", "cherry"]

for x in fruits :
  print(x)
  if x=="banana":
    break
  

########################
print()


fruits = ["apple", "banana", "cherry"]
for x in fruits :
  if x=="banana":
    break
  print(x)


##################
print()
#################

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#####################
print()
############
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="banana":
    continue
  
  print(x)

#########################
print()
#####################


for x in range(16):
  print(x)


print()

###########################

for x in range(2,9):
  print(x)

#####################
print()


##The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2,30,3):          #difference 3 in input by using third parameter in range
  
  print(x)

##################
print()


for x in range(6):
  print(x)
else:
  print("Finally Finished!")

print()

##############

for x in range(6):
  if x == 3:  break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

##########################
print()

for x in range(9):
  if x==5: break
  print(x)
else:
  print("Finally finished")


print()
###########

for x in range(9):
  if x==7: break
  print(x)
else:
  print("Finally finished")

##################
print()


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x,y)


print()


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x,y)

print()
#############


for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement


