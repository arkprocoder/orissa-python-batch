
def employee(name,salary):
    bonus=10000
    print(f"Hello {name} \nYour Salary is Credited {salary} Rs")
    amount=salary+bonus
    return amount
    

e1=employee("Anjeli",50000) #e1=60000
e2=employee("Nahak",150000) #e2=160000
e3=employee("Lipsa",250000) #e3=260000
print("Total Revenue=",e1+e2+e3)