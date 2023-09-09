
import json
#some JSON
x='{"name":"Rahul","age":20,"city":"BBSR"}'

#parse x:

y=json.loads(x)

#the result is python dictionary

print(y["age"])


###############################

import json

x='{"name":"aman","age":10,"city":"delhi"}'
y=json.loads(x)
print(y["name"])


###############################

import json

x='{"name":"Ravi","age":88,"city":"bbsr"}'
y=json.loads(x)
print(y["city"])


#######################################


import json

x='{"name":"vivek","age":66,"city":"mumbai"}'
y=json.loads(x)
print(y["name"])


print()
##########################

import json

#a python object

x={
    "name":"Michel",
    "age":23,
    "city":"Chennai"
}

#convert into JSON
y=json.dumps(x)

#the result is JSON String
print(y)



##############################

import json

# a python object(dict)

x={
    "name":"vikram",
    "age":30,
    "city":"bbsr"
}

y=json.dumps(x)
print(y)

########################

import json

x={
    "name":"Gautam",
    "age":40,
    "city":"chennai"
}

y=json.dumps(x)
print(y)


#######################

import json
x={
    "name":"lucky",
    "age":60,
    "city":"delhi"
}
y=json.dumps(x)
print(y)



#################################

import json

print(json.dumps({"name":"John","age":30}))
print(json.dumps(["apple","bananas"]))
print(json.dumps(("apple","banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


####################################

import json

x={
    "name":"Rahul",
    "age":30,
    "city":"bbsr",
    "married":True,
    "divorced":False,
    "childen":("Lucky","Aman"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1}
    ]
}
y=json.dumps(x)
print(y)

print()

#########################

import json

x={
    "name":"Aman",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("lucky","ricky"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":28.9}
    ]
}

print(json.dumps(x,indent=4))

#########################

print()


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


print()

################################

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=4,separators=(".","=")))

print()

import json

x={
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "childen":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"bmw 230","mpg":28.9},
        {"model":"Ford","mpg":56.9}
    ]
}

print(json.dumps(x,indent=4,sort_keys=True))

print()

####################################



















































