class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print()

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x=self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print()

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print()

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print()

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print()
################

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a += 1
        return x

myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print()

# StopIteration
# Stop after 20 iterations:

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumber()
myiter = iter(myclass)

for x in myiter:
    print(x)


print()

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a += 1
            return x
        else:
         raise StopIteration
        
myclass = MyNumber()
myiter = iter(myclass)

for x in myclass:
    print (x)


###################
print()
#############

class MyNumber:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a <= 14:
            x=self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumber()
myiter = iter(myclass)

for x in myclass:
    print(x)

print()
######################

class MyNumber:
    def __iter__(self):
        self.a = 1 
        return self
    
    def __next__(self):
        if self.a <= 10:
            x=self.a
            self.a += 1
            return x
        
        else:
            raise StopIteration
    
    myclass = MyNumber()
    myiter = iter(myclass)

    for x in myclass:
        print(x)























