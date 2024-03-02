a=[1,2,3,4,5,6,7]
b=[8,9,2,3,4,5,10]
# res=list(filter((lambda x:x not in b),a))
res=list(filter((lambda x:x in b),a))
print(res)