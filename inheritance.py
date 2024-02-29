# single level inheritance
# multi level inheritance



class GrandParent:
    def gproperties(self):
        print('grand Parent Property')
    
    def gbusiness(self):
        print('grand Parent Business')


class Parent(GrandParent):
    family_name='shettys'

    def properties(self):
        print('Parent Property')
    
    def business(self):
        print('Parent Business')
    
class Child(Parent):
    child_name="chandan"

    def childproperty(self):
        print("child property")
    
    def childbusiness(self):
        print("child business")

obj1=Child()
print(obj1.family_name)
obj1.properties()
obj1.business()
obj1.childproperty()
obj1.childbusiness()

obj2=Parent()