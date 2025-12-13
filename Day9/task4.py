#create a multiple function for arithmetic operations like add,subtract,multiply,divide and ask the user to perform which operation to be done and do the task as per user input
def sum(a,b):
      return a+b
def sub(a,b):
        return a-b
def mul(a,b):
        return a*b
def div(a,b):
            return a/b
        
def main_fun(a,b):
    operation=input("Enter the operation to be performed(add,sub,mul,div): ")
    if operation=="add":
        print("Sum is:",sum(a,b))
    elif operation=="sub":
        print("Difference is:",sub(a,b))
    elif operation=="mul":
        print("Product is:",mul(a,b))
    elif operation=="div": 
        try:
          print("Quotient is:",div(a,b))
        except:
             print("Value Error")
    else:
        print("Invalid operation")
try:        
  a=int(input("Enter first number:"))
  b=int(input("Enter second number:"))
except ValueError:
    print("Enter a number ")  
main_fun(a,b)
