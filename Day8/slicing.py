#"student" if i want to print only uden if st-uden-t then i use slicing of string
a="student" 
b=a[2:6:2]
print(b)
#for slicing use : 
c="This is string"
print(c[:5])
print(c[:])
print(c[::])
print(c[5:])
print(c[-7:-1])
#methods of string slicing
#find()
print(c.find('i'))
print(c.upper())
print(c.lower())
print(c.count('i'))