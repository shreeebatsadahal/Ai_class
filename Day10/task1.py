#write a program to ask the two number from user and perfrom divison   operation

try:
    a=int(input("num :"))
    b=int(input("num :"))
    div=a/b
except ValueError: #you can put condition aswell
    print("ValueError")
except TypeError: #you can put condition aswell
 print("TypeError")
except ZeroDivisionError: #you can put condition aswell
    print("ZeroError")
else:     
    print(div)
finally:
   print("ended") 