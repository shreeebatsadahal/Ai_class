def sum(a,b):
    return a+b           #return stored to the function
result = sum(5,3)      #function called and returned value stored in result variable
print("Sum is:",result)
print(sum(5,3))

def sum(a=9,b=3):#default parameters
    return a+b  
result = sum()      #function called and returned value stored in result variable
print("Sum is:",result)

#default parameters should be at the end of the parameter list
def sum(a,b=3):#default parameters
    return a+b
result = sum(5)      #function called and returned value stored in result variable
print("Sum is:",result)
  