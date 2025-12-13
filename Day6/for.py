#range function: [start,end)
for i in range(5): #while giving single number it understands as start from 0 and end in 5
    print(i)
for i in range(10,21): #range can adjust 3 things start,end,step range(0,10,2)
    print(i)

# a="shreebatsa"
# for i in a:
#  print (i)

for i in range(7,101,7):
    print(i)
#write a program to calculate the number of vowels from the text"python programming is fun if you learned properly"
texts="python programming is fun if you learn it properly"
vowels="aeiou"
count=0
for character in texts:
    if character in vowels:
        count=count+1
print(f"The no of vowels in {texts} is {count}")   