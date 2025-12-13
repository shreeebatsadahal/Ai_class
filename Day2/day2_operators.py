#operators are
'''
+additon
- subtraction
* multiplication
/ division
% modulus remainder
// floor division round off to nearest whole number 7/2=3.5 7//2=3  
** exponentiation for power rasied-2 to the power 4 is written as 2**4  

'''
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))     
x2=int(input("Enter x2: ")) 
y2=int(input("Enter y2: "))
a=( (x2-x1)**2 +(y2-y1)**2)**0.5
print(a)

##by using math module  
import math #when you import write it at the top of the code 
a=math.sqrt( (x2-x1)**2 +(y2-y1)**2)
print(f"{a:.3f}")  #to print only 3 decimal places      

#logical operators returns true of false
'''
and if both true then true
or if any one true then true
not if true then false if false then true   
'''
