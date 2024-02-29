class Employee:
    # initialise the data members
    companyName=None
    since=None
    #method is initialise
    def companyDetails(self):
        return f"\nCompany Name is {self.companyName}\nSince {self.since} \nEMployee name {self.employeeName}"
    
# create objects for the class Employee
e1=Employee()
e1.companyName='Infosys'
e1.since=1999
e1.employeeName='abc'
print(e1.companyDetails())
e2=Employee()
e2.companyName='TCS'
e2.since=1995
e2.employeeName='jik'
print(e2.companyDetails())
e3=Employee()
e3.companyName='Wipro'
e3.since=1993
e3.employeeName='rajesh'
print(e3.companyDetails())
print(e3.employeeName)