#task create a class CAR  with properties brand,model,ev or diesel with methods: start, stop, brake, and carinfo to print the attributes of the car

class Car:
    def __init__(self, brand, modelnumber, fueltype):
        self.brand = brand
        self.modelnumber = modelnumber
        self.fueltype = fueltype

    def start(self):
        print(f"{self.brand} car is starting")

    def stop(self):
        print(f"{self.brand} car is stopping")

    def brake(self):
        print(f"{self.brand} car is braking")

    def carinfo(self):
        print(f"Car Brand: {self.brand}\nModel Number: {self.modelnumber}\nFuel Type: {self.fueltype}")

car1 = Car("Toyota", "2020", "EV")
car1.start()
car1.carinfo()
car1.stop()