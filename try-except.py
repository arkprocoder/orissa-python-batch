a=10
b=2
# print(a/b)

try:
    print(a/b)
except Exception as e:
    print("i cant divide a number with zero",e)
else:
    print(' i am going to execute else block only if try is getting passed')

finally:
    print("i am going to run 100 if try pass or except fails")