mydict={
    "employeeName":"Anees",
    "employeeRole":"Full stack developer",
    "since":2020,
    "salary":50000.25,
    "skills":["python","java","react","angular"],
    "interest":{"cricket","gym","teaching"},
    "isActive":True
}

# print(mydict)
# print(mydict.keys())
# print(mydict.values())
# print(mydict.get("skills"))
# print(mydict.get("employeeRole"))
mydict.update({
    "PhoneNumber":7854123698
})
mydict.update({
    "salary":987000.25
})

print(mydict)

mydict2=mydict.copy()
print("Dictionary copy", mydict2)

mydict2.clear()
print(mydict2)