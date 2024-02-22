class Employee:

    # data members of the class
    companyName="GUVI"
    since=2014

    #methods of the class
    def holidays(self):
        print("August 15Th Holiday")


e1=Employee()
e2=Employee()

# print(e1.companyName)
# print(e1.since)
# e1.holidays()
# print("\n")
# print(e2.companyName)
# print(e2.since)
# e2.holidays()

e1.employeeName="Ark"
e1.role="Full stack developer"
e1.salary=50000
e1.age=26

e2.employeeName="Rohan"
e2.role="Front End developer"
e2.salary=60000

print(e1.companyName)
print(e1.since)
print(e1.employeeName)
print(e1.salary)
print(e1.role)
print(e1.age)
e1.holidays()
print("\n")
print(e2.companyName)
print(e2.since)
print(e2.employeeName)
print(e2.role)
print(e2.salary)
e2.holidays()