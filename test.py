# num = 10
# str_num = str(num)
# print(str_num)  # Output: '10'
# print(type(str_num)) #stringconverted


# str_num = '10'
# num = int(str_num)
# print(num)  # Output: 10

# bool_val = True
# str_bool = str(bool_val)
# print(str_bool)  # Output: 'True'

# bool_val = True
# int_bool = int(bool_val)
# print(int_bool)  # Output:


# str_bool = 'True'
# bool_val = bool(str_bool)
# print(bool_val)  # Output: True

# skills = list(input("Enter skills separated by comma: ").split(","))

# # Print the list of skills
# print("Skills:", skills)

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# salary = float(input("Enter your salary: "))

# print("Name:", name, "| Data type:", type(name))
# print("Age:", age, "| Data type:", type(age))
# print("Salary:", salary, "| Data type:", type(salary))
# name=input("Enter Student Name:\n")

# mark=[]
# english=int(input("Enter english mark it should be in the range (0-100)\n"))
# mark.append(english)
# maths=int(input("Enter maths mark it should be in the range (0-100)\n"))
# mark.append(maths)
# science=int(input("Enter science mark it should be in the range (0-100)\n")) 
# mark.append(science)
# social=int(input("Enter social mark it should be in the range (0-100)\n"))
# mark.append(social)
# tamil=int(input("Enter tamil mark it should be in the range (0-100)\n"))
# mark.append(tamil)
# hindi=int(input("Enter hindi mark it should be in the range (0-100)\n"))
# mark.append(hindi)

# percentage=sum(mark)/6
# print(percentage)

# if(percentage>=90 and percentage<100):
#     print("Excellent")
#     print("Grade 'A+'")
# elif(percentage>=75 and percentage<90): 
#     print("Good")
#     print("Grade 'A'")
# elif(percentage>=60 and percentage<75):
#     print("Average")
#     print("Grade 'B' ") 
# elif(percentage>=55 and percentage<60):
#     print("Pass")
#     print("Grade 'C'") 
# else:
#     pass
# def areaOfSquare(length):
#     area=length*length
#     return area

# length=int(input("Enter length of square\t"))
# area=areaOfSquare(length)
# print(f'Area of square is {area}')

# #2)d)area of triangle
# def areaOfTriangle(base,height):
#     area=(base*height)/2
#     return area

# base=int(input("Enter base of triangle\t"))
# height=int(input("Enter height of triangle\t"))
# area=areaOfTriangle(base,height)
# print(f'Area of triangle is {area}')

class Laptop:
    def __init__(self,deviceName,processor,installedRam,deviceID,productId,systemType,manufuctureDate) :
        self.deviceName=deviceName
        self.processor=processor
        self.installedRam=installedRam
        self.deviceID=deviceID
        self.productId=productId
        self.systemType=systemType
        self.manufuctureDate=manufuctureDate

    def printDetails(self):
        print(f'\nDeviceName={self.deviceName}\n Processor={self.processor}\n InstalledRam={self.installedRam}\nDeviceID={self.deviceID}\n ProductId={self.productId}\n SystemType={self.systemType}\nManufuctureDate={self.manufuctureDate}\n--------------------\n')    


l1=Laptop(" Dell XPS 15","Intel Core i7-10750H"," 16GB DDR4"," XYZ123","DELLXPS15-2024","Windows 10 Pro 64-bit"," 2023-06-15")
l2=Laptop("MacBook Pro 13","Apple M1 Pro","16GB unified memory","JKL345","MACBOOKPRO13-2024","macOS Monterey","2023-10-05")
l3=Laptop("HP","Intel","64GB","klj12","hp-2021","window","2021-03-12")
l1.printDetails()
l2.printDetails()
l3.printDetails()