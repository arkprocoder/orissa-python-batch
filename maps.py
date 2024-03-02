# numbers=[1,2,3,4,5]
# res=list(map((lambda x:x**2),numbers))
# print(res)

def square(a):
    return a*a
def cube(a):
    return a*a*a

functions=[square,cube]
numbers=[2,3,4,5,6]

for i in numbers:
    res=list(map((lambda x:x(i)),functions))
    print(res)