#tuple is immutable
tuple1=(1,True,3,"shree",5.37) #we can put heterogenous data type in tuple
print(type(tuple1))
list1=[1,True,3,"shree",5.37] #we can put heterogenous data type in list
print(tuple1)
tuple2=(1,2,3,4,5)
print(tuple1+tuple2) #concatenation of tuples but why? coz it creates a new tuple
#packing and unpacking of tuples
mytuple=1,2,4 #packing
print (mytuple)
a,b,c=mytuple #unpacking
print(a) 
print(b)
print(c)   

#you can convert list to tuple and tuple to list (type casting of tuples and lists)
list2=[5,6,7,8]
tuple3=tuple(list2) #list to tuple
print(tuple3)
list3=list(tuple3) #tuple to list'
print(list3)
