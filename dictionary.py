
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

mydetails.update({
    "salary":60000,
    "age":27
})
print(mydetails)

print(mydetails.get("age"))
print(mydetails.keys())
print(mydetails.values())

mydetails2=mydetails.copy()
print(mydetails2)

# clear