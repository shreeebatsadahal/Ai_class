# """
# OOP Aspect: Inheritance
# =======================
# Inheritance allows a class to inherit properties and methods from another class.
# This helps with code reuse and logical hierarchy.
# """


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says: Woof!")


# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says: Meow!")


# # Usage
# animals = [Dog("Buddy"), Cat("Whiskers"), Animal("Creature")]
# for animal in animals:
#     animal.speak()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent's constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Calling parent's speak() before overriding
        print(f"{self.name} says: Woof! (Breed: {self.breed})")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Inheriting initialization
        self.color = color

    def speak(self):
        super().speak()
        print(f"{self.name} says: Meow! (Color: {self.color})")


# Usage
animals = [Dog("Buddy", "Golden Retriever"), Cat("Whiskers", "White")]

for animal in animals:
    animal.speak()