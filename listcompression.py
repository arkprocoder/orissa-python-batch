# data=[]
# for i in range(100):
#     if(i%2==0):
#         data.append(i)
# print(data)

data= [i for i in range(100) if i%2==0]
print(data)

data= {i for i in range(100) if i%2==0}
print(data)

data= (i for i in range(100) if i%2==0)
print(data)