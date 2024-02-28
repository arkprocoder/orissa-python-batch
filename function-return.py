# 100000 lakh to ankita to get me iphone 

# def ankita(money):
#     return "iphone"


# anees=ankita(100000)
# print(anees)
data=[]
company="infosys"
def employee(name,salary):
    bonus=10000
    print(f"Employee Name is {name}\n Employee  salary is {salary+bonus}")
    return bonus+salary

emp1=employee('rohan',40000)
data.append(emp1)
emp2=employee('rahul',50000)
data.append(emp2)
emp3=employee('harshith',150000)
data.append(emp3)
emp4=employee('meghana',250000)
data.append(emp4)

print(sum(data))
