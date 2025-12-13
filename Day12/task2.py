class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
class Student(Person):
    def __init__(self,name,age,roll,section):
        super().__init__(name,age)
        self.roll=roll
        self.section=section
    def student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll}, Section: {self.section}")
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def teach(self):
        print(f"I teach {self.subject}")
##creating object
s1=Student("Alice",20,"101","A")
t1=Teacher("Mr. Smith",40,"Mathematics")
s1.student_info()
s1.introduce()

t1.teach()
