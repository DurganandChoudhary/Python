decibels = float(input("Enter a sound level in decibels: "))
if decibels >= 130:
    print ("Jackhammer")
elif decibels >= 106:
    print ("Gas Lawnmower")
elif decibels >= 70:
    print( "Alarm Clock")
elif decibels >= 40:
    print ("Quiet Room")
else:
    print ("Noise level below the quietest noise in the table")
