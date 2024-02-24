# def calculator(a,b):
#     print(a+b)
    
# def calculator(a,b,c):
#     print(a+b+c)


class Calculator:
    def add(self,*args):
        result=0
        for n in args:
            result=result+n
        return result
    

obj=Calculator()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1,2,3,4))
print(obj.add(1,2,3,4,5))

