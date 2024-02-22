#single level inheritance without constructor
class Parent:
    family_name="shettys"

    def property(self):
        print("Parent property")

    def business(self):
        print("Parent business")

class Child(Parent):

    child_name="Chandan"

    def childproperty(self):
        print("Child property")

    def childbusiness(self):
        print("Child business") 

obj=Child()
obj.property()
obj.business()
obj.childbusiness()
obj.childproperty()

obj2=Parent()