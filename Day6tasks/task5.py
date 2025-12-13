a=int(input("Enter a number"))
i=1
if a<0:
   print("The factorial of negative no is none")
elif a==1 or a==0:
   print(f"The factorial of {a} is 1") 
else:
    fact=1
    for i in range(1,a+1):
        fact=fact * i
print(f"factorial is {fact}")