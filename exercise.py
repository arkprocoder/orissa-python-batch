'''
1. Write  a program to take the inputs from the User
"employeeName":"Anees",
"employeeRole":"Full stack developer",
"since":2020,
"salary":50000.25,
"skills":["python","java","react","angular"],
"interest":{"cricket","gym","teaching"},
"isActive":True

read the inputs

update the salayry to 100000 by taking input update and print it

input : which key values you want to print? skills
'''
employeeName=input("Enter the EMployee Name:\n")
employeeRole=input("Enter the EMployee Role:\n")
employeeSalary=input("Enter the EMployee Salary:\n")
employeeSkills=input("Enter the EMployee skills:\n")
employeeInterest=input("Enter the EMployee interest:\n")
employeeStatus=input("Is Employee is Active:\n")
employeeSalary=float(employeeSalary)
employeeSkills=employeeSkills.split()
employeeInterest=set(employeeInterest.split())
employeeStatus=bool(employeeStatus)

mydetails={
    "Name":employeeName,
    "Role":employeeRole,
    "Salary":employeeSalary,
    "Skills":employeeSkills,
    "interest":employeeInterest,
    "status":employeeStatus
}
print(mydetails)

updSalary=input("Enter the Employee Salary to be updated:\n")
mydetails.update({ "Salary":float(updSalary)})
print(mydetails)

key=input("Enter the key value which you want to fetch:\n")
print(mydetails.get(key))