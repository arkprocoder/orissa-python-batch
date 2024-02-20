mystr="welcome to day-2 Session on Python"

# inbuilt methods of string
print("Uppercase",mystr.upper())
print("Lowercase",mystr.lower())
print("index",mystr.index('day'))
print("index",mystr.index('o'))

print("capitalize",mystr.capitalize())
print("count",mystr.count('o'))
print("count",mystr.count('Python'))
print("find",mystr.find('anees'))

print("startswith",mystr.startswith("Welcome"))
print("endswith",mystr.endswith("Python"))
print("length",len(mystr))
print(mystr.isalpha())

print("replace",mystr.replace("Python","Java"))
print("split",mystr.split())


mystr="My skills is Programming"
mystr=mystr.upper()
print(mystr)