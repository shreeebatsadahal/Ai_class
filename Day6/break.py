# for i in range(5):
#     if i == 3:
#         break #skips once condition is true
#     print(i)
for i in range(5):
    if i == 3:
        continue #continue skips correct itteration
    print(i)

#to print 10-20 even
for i in range(11,20):
    if i%2!=0 :
     continue
    print(i)
#ask a no from user and multiple of table
a=int(input("Enter the no"))
for i in range(1,11): 
   print(f"{a} *{i}={a*i}")