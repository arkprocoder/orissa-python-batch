from abc import ABC,abstractmethod

#Abstarct class 
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        print(3.14*self.radius*self.radius)


    def perimeter(self):
        print(2*3.14*(self.radius))

obj1=Circle(5)
obj1.area()
obj1.perimeter()