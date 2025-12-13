# a="ShreebatsaDahal"
# print(f"The length of a is: {len(a)}") # prints the length of the string



a=input("Enter your password of atleast 8 -20characters: ")
b=8<len(a)
c=len(a)<20
print(f"You can only use password if its length>8: {b}")
print(f"You can only use password if its length<20: {c}")
#write a default password and check whether the user input matches the default password if it matches false
defaultpassword="123456789"
print(f"You may only use the password if its True: {a!=defaultpassword}")   