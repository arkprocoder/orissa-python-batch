from abc import ABC,abstractmethod

class Iphone16(ABC):

    @abstractmethod
    def drone(self):
        pass

    @abstractmethod
    def fivecamera(self):
        pass

    @abstractmethod
    def sliding(self):
        pass

    # @abstractmethod    
    def automaticCharge(self):
        pass

class Implementation16(Iphone16):
    
    def drone(self):
        print("I have implemented Drone")

 
    def fivecamera(self):
        print("I have implemented 5 cameras")

   
    def sliding(self):
        print("I have implemented Sliding in iphone 16")

phone=Implementation16()