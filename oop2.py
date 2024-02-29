# Constructor?
class Company:
    def __init__(self,employeeName,age,address,role,experience,phone):
        # set the values for data members
        self.eName=employeeName
        #datamember varaiable = pass by value by temporary varaible
        self.age=age
        self.address=address
        self.role=role
        self.experience=experience
        self.phone=phone
        print("I have set all the values for data members for ",employeeName)

    def employeeDetails(self):
        return f'\nEmployee Name is {self.eName}\nEmployee Age is {self.age}\nEmployee address is {self.address}\nRole is {self.role}\nExperience is {self.experience}\nPhone number is {self.phone}'
    
    @staticmethod
    def greeting():
        print("Good Evening")

e1=Company("Rohan",25,"Bangalore",'Python Developer',2,'9874563210')
print(e1.employeeDetails())
e2=Company("Ankit",28,"Chennai",'Java Developer',3,'9674563210')
print(e2.employeeDetails())
print("particaly i need specific value")
print(e2.phone)
e2.greeting()