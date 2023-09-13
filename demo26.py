


##########################
username=input("Enter username: ")
print("Username is: "+username)


print()
#################


price =49
txt="The price is {} dollars"
print(txt.format(price))

#################

price =99
txt ="the price is {} dollars"
print(txt.format(price))

#################

price=987
txt="the price is {:.2f} dolaars"
print(txt.format(price))

#################

quantity=3
itemno=569
price=741

myorder="I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity,itemno,price))

#################

quantity=3
itemno=569
price=741

myorder=" i want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity,itemno,price))



#################

'''age=28
name="Rahul"

txt="His name is {1}. {1} is {0} years old."
price(txt.format(age,name))
'''
myorder="I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford",model="Mustang"))


#################




















