# Create a Car class with the following attributes and methods:
# Attributes: make, model, year, color, mileage.
# Methods:
# init(self, make, model, year, color): Constructor method to initialize the attributes.
# start(self): Method that simulates starting the car.
# stop(self): Method that simulates stopping the car.
# drive(self, miles): Method that simulates driving the car for a certain number of miles.
# Create an instance of the Car class and demonstrate its functionality by starting the car, driving it, stopping it, and displaying the car's information.


class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.mileage=0
        self.is_running=False

    def start(self):
        if not self.is_running:
            self.is_running=True
            print(f"The {self.year} {self.make} {self.model} is now Running")
        else:
            print("The car is already running....")
    
    def stop(self):
        if self.is_running:
            self.is_running=False
            print(f"The {self.year} {self.make} {self.model} is now Stop")
        else:
            print("The car is already stopped...")

    def drive(self,miles):
        if self.is_running:
            self.mileage+=miles
            print(f"The car has driven {miles} miles..")
        else:
            print("the car has been stopped you cannot drive")
        

    def display(self):
        print(f"Car Information:\n{self.year} {self.model} {self.color} \nMilage {self.mileage} miles")

mycar=Car("BMW","bmw10series",2023,"Black")

mycar.display()
print("\n")
mycar.start()
mycar.start()
mycar.drive(100)
mycar.stop()
mycar.stop()