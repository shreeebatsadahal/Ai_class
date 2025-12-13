#is,is not,==
a=300
b=300
print(f"a is b: {a is b}")
li1=[1,2,3]
li2=[1,2,3]
li1=li2
print(f"li1 is li2: {li1 is li2}")
#less than 256 value of variables are stored in the same memory location then python puts it on the same block
#== checks content of the list and is checks list memory location/object