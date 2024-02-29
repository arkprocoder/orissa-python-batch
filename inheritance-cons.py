# single level inheritance with constructor
class Company: #base class or parent class
    # initializing the constructor
    def __init__(self,name,location,dcbranch):
        # setting the values
        self.name=name
        self.location=location
        self.dcbranch=dcbranch
        print("I have set the values for class Company")

    def companyDetails(self):
        return f"\nCompany Name is {self.name}\nCompany located at {self.location}\nDc Branch {self.dcbranch}"

# archive the single level inheritance

class Employee(Company):

    # initalizing the constructor to child class or derived class
    def __init__(self,name,location,dcbranch,empid,employeeName,employeeRole):
        # setting the values for child class
        # self.name=name
        # self.location=location
        # self.dcbranch=dcbranch
        super().__init__(name,location,dcbranch)
        self.empid=empid
        self.employeeName=employeeName
        self.employeeRole=employeeRole
        print("I have set the values for class Employee")

    def employeeDetails(self):
        return f"\nCompany Name is {self.name}\nCompany located at {self.location}\nDc Branch {self.dcbranch}\nEmployee Id is {self.empid}\nEmployee Name is {self.employeeName}\nEmployee Role is {self.employeeRole}"
    


# c1=Company("Guvi","chennai","IIT madras")
# companydata=c1.companyDetails()
# print(companydata)

emp1=Employee("Guvi","chennai","IIT madras","GUVI123","Anees","Full stack mentor")

Companydetails=emp1.companyDetails()
print(Companydetails)

Employeedetails=emp1.employeeDetails()
print(Employeedetails)