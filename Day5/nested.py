
a=int(input("Enter your marks from 0 to 100:"))
if(a>=50):
    print("You have passed")
    if(a>=90):
        print("Your grade is A")
    elif(80<=a<90):
        print ("Your grade is B")
    elif(70<=a<80):
        print ("Your grade is C")
    else:
        print ("Your grade is D")
else:
    print ("You have failed")


