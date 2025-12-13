#args and kwarg
# *args helps to send many arguments 
def myfun(args): #args only sends one argument
    print(args)
myfun    
myfun(1)

def myfun(*args): #*args sends many argu
    print(f" my 3rd argu is {args[2]}") #as it is a tuple can use indexing

myfun    
myfun(1,23,4,5,6) #positional argument returns value in tuple

print('''       ''')
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(f"the sum is {sum}")
add(5,6,7)
add(1)
add(5,10)
print("        ")
#kwargs
def kwarg(**kwargs): #kwargs and args are js the variable name you can use anything after *
    for key,value in kwargs.items():
      print(f"{key}: {value}")
kwarg(name="shree",add="brt")
#kwargs give value in dict
#combination of kwargs and ask
def funn(*args,**kwargs):
    print(args)
    print(kwargs)
funn("shreebatsa","dahal",city="brt",state="koshi",country="Nepal")    

def funn(*args,**kwargs):
    for i in args:
      print(i)
    print()
    for key,value in kwargs.items():
         print(f"{key}: {value}")
  
funn("shreebatsa","dahal",city="brt",state="koshi",country="Nepal")    