def generator(n):
    for i in range(n):
        yield i

res=generator(10)
print(res)

print(res.__next__())
print(res.__next__())

def greeting():
    print("Hello Good Evening")
    print(res.__next__())
    print(res.__next__())

def close():
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
   



greeting()
close()

print('ii am done')
# print(res.__next__())