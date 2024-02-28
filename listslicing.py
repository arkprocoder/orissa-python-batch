# mylist=['anees','meghana','amrutha','aneeqah','aadithyaa','harshith']
# mylist.sort()
# print(mylist)
# mylist.remove('anees')
# print(mylist)

# print("positive slicing")
# myslice=[1,2,4,6,7,9,10]
# print(myslice[:]) #[1,2,4,6,7,9,10]
# print(myslice[1:]) # [2,4,6,7,9,10]
# print(myslice[:5]) # [1,2,4,6,7]
# print(myslice[3:7]) # [6,7,9,10]

# print('negative slicing')
# # [1,2,4,6,7,9,10]
# myslice=[1,2,4,6,7,9,10]
# 10= -1  = 6
# 9= -2   = 5
# 7= -3   = 4
# 6= -4   = 3
# 4= -5   = 2
# 2= -6   = 1
# 1= -7   = 0

# print(myslice[-1])
# print(myslice[-2])
# print(myslice[-3])
# print(myslice[1])
# print(myslice[2])
# print(myslice[3])
# myslice=[1,2,4,6,7,9,10]
# print(myslice[-5:]) # [4,6,7,9,10]
# print(myslice[1:-3]) # (start, end-1) (1,-3-1),(1,-4) # [2,4,6]
# print(myslice[:-1]) # (start, end-1) (0,-1-1),(0,-2) # [1,2,4,6,7,9]
# print(myslice[-5:-2]) 

# myslice=[1,2,4,6,7,9,10]
# print(myslice[::2]) # [1,4,7,10]

# print(myslice[::-1])
# print(myslice[::-2])

myslice=[1,2,4,6,7,9,10]
print(myslice[-5:-1]) #4,6,7,9
print(myslice[-6:-4]) #4,6,7,9