from functools import reduce

# x=[1,2,3,4,5,6] #list i can iterate these values
# # syntax reduce((function),iterable)
# res=reduce((lambda x,y:x*y),x) 
# print(res)

#x=[1,2,3,4,5,6] x=1 y=2    y:1*2  y=2 
#x=[2,3,4,5,6] x=2 y=3    y:2*3  y=6 
#x=[6,4,5,6].........
# x=[720]

def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

numbers=[1,2,3,4,5,6]

sumres=reduce(add,numbers)
print(sumres)

minres=reduce(sub,numbers)
print(minres)

mulres=reduce(mul,numbers)
print(mulres)