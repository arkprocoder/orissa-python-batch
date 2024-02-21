# 5! = 5*4*3*2*1 =120

# 10! = 10*9*8*7*....*1

# 1! = 1 

def factorial(n):  
    if(n==1):
        return 1   
    return n*factorial(n-1)

n=int(input("Enter the number to find its factorail...\n"))
output=factorial(n)
print(output)



# 2. 
# def factorial(5):  
#     if(5==1):
#         return 1   
#     return n*factorial(n-1)
#     return 5*factorial(4)


# def factorial(4):  
#     if(4==1):
#         return 1   
#     return n*factorial(n-1)
#     return 5*4*factorial(4-1)
#     return 5*4*factorial(3)


# def factorial(3):  
#     if(3==1):
#         return 1   
#     return n*factorial(n-1)
#     return 5*4*3*factorial(2)

# def factorial(2):  
#     if(2==1):
#         return 1   
#     return n*factorial(n-1)
#     return 5*4*3*2*factorial(1)

# def factorial(1):  
#     if(1==1):
#         return 1   
#     return n*factorial(n-1)
#     return 5*4*3*2*1 =120
