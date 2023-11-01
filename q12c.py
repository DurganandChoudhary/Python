s = int(input("Please enter the number of rows :  "))  
for i in range(0, s + 1):  
    for j in range(s - i, 0, -1):  
        print(j, end=' ')  
    print()  