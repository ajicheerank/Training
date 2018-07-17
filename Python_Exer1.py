x=int(input("Enter any number: "))

if x < 10:
    print ("This is a good number")
elif x < 100 and x%2 != 0:
    print ("This is a better number")    
elif x < 100 and x%2 == 0:
    print ("This is the best number")
else:
    print ("Horrible number")