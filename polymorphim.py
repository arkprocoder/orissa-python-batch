class Human:
    def __init__(self,name):
        self.name=name

    def introduce(self):
        print('Hello my name is ',self.name)  

class Teacher(Human):
    def perform(self):
        print(self.name,'is teacher')

class Student(Teacher):
    def perform2(self):
        print(self.name,'is student')

obj=Student('anees')
obj.introduce()
obj.perform()
obj.perform2()

