class Animal:
    def speak(self):
        print('Animal doesnt not speak')

class Dog(Animal):
    # def speak(self):
    #     print('DOg Barks')
    pass

class Cat(Animal):
    def speak(self):
        print('Cat meow')


obj=Dog()
obj.speak()

