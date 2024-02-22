class Employee:

    # data members of the class
    companyName="GUVI"
    since=2014

    #constructors
    def __init__(self,name,role,salary,location):
        # print("i am a constructor i will execute compulsory whenever a object is created ")
        self.name=name
        self.role=role
        self.salary=salary
        self.location=location
        # print("i have set the values for",{self.name})

    # methods
    def employeeDetails(self):
        return f"\nEmployee Name is {self.name}\nEmployee Role is {self.role}\nEmloyee Salary is {self.salary}\nLocation is {self.location}"

    @staticmethod
    def greeting():
        print("Good Evening...",)

obj1=Employee("Anjeli","frontend developer",45000,"chennai")
obj2=Employee("Bhumika","Backend developer",55000,"chennai")

print(obj1.employeeDetails())
print(obj2.employeeDetails())

obj1.greeting()