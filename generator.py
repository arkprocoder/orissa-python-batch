def generator(n):
    for i in range(n):
        yield i 

res=generator(5)
print(res)
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
# print(res.__next__())