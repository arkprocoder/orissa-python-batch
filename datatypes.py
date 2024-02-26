'''
firstName='Rohan'
lastName="Sharma"
print(firstName,lastName)
print(type(firstName),type(lastName))
age=21
phoneNumber=987456321457
salary=50125.60
print(age,type(age))
print(phoneNumber,type(phoneNumber))
print(salary,type(salary))
'''
# fname='rohan'
# lname='shetty'
# fname='rohit'
# lname='sharma'
# print(fname,lname)

# boolean data type
isActive=True
isActive='False'
print(type(isActive))
isActive=bool(isActive)
print("Type casting",type(isActive))


# mynum="12345"
# mynum=int(mynum)
# print(mynum,type(mynum))

# mynum2="453ark"
# mynum2=int(mynum2)
# print(mynum2,type(mynum2))

# list
# myskills=['python',"java",123,5.0,True,[4,5,6]]
# print(myskills)
# print(type(myskills))
# print(myskills[3])

# set
# myset={1,2,3,4,1,2}
# print(myset)
# print(type(myset))

# tuple
# mytup=(1,2,3)
# print(type(mytup))

mydetails={
    "name":"rohan", #key:value
    "age":25,
    "location":"Bangalore",
    "skills":["java","python"],
    "habbits":{"dancing","sleeping"},
    "isActive":True,
    "salary":50000.0,
    "companies":('infosys','tcs')
    
    }

print(mydetails)
print(type(mydetails))


a=None
print(type(None))
