class Father:
    def __init__(self,name):
        self.name=name
        print('father')

    def provide(self):
        return f"father {self.name} provides for family"


class Mother:
    def __init__(self,name):
        self.name=name
        print('mother')

    
    def provide(self):
        return f"mother {self.name} provides for family"
    

class Child(Father,Mother):
    def __init__(self,name):
        super().__init__(name)
        # Mother.__init__(self,name)
    
        
    # def provide(self):
    #     return f"child {self.name} provides for family"


obj=Child("rohan")
print(obj.provide())