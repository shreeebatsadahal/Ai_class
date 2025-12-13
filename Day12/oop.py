#class Class_name:  class keyword is used to delcare class and classname fst letter should be capital

class Student:
    name="Student_name" #class variable
    age=20    #here you keep properties of the class
    roll_no="007"
    section="A"
s1=Student() 
s2=Student() #object creation
print(s1.name) #dot operator is used to access the class variable
print(s2.name)  #this method is not used as in every class you will get the same value of nepal

print("                                            ")
#constructor function: You dont need to call the constructor function it will be called automatically when the object is created
class Student:
    def __init__(self,name,roll,address): #self is used to refer to the current object
        self.name=name  
        self.roll=roll
        self.address=address
        print(self.name,self.roll,self.address)
        #creating a method to display student info
    def studentinfo(self):
        print(f"Name:{self.name} \n Roll no:{self.roll} \n Address:{self.address}")    
         #constructor function
s3=Student("shree","101","brt")         
s3.studentinfo()  #method calling using object
         
s4=Student("ram","102","ktm" )         
 #when the object is created the constructor function is called automatically  
#you need to enter the values of name,roll,address when creating the object
#class bhitra function=method,class bhitra obj properties=attributes

