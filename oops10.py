# polymorphism
# poly=many
class Human:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print("my name is ",self.name)

class Teacher(Human):
    def performAcivity(self):
        print(f"{self.name} is teaching")

class Student(Human):
    def performAcivity(self):
        print(f"{self.name} is student")
    

john=Teacher("John")
allien=Student("allein")

people=[john,allien]
for p in people:
    p.introduce()
    p.performAcivity()