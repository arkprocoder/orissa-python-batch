# Evaluate mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
# 1)write a python program to evaluate below list
# a)Add the items in list 
# b)Find the length of the list
# c)sort the elements from the list
# d)reverse the list
# e)Count the duplicates elements from the list (3,2)

mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
mylist.append(15)
print("appending",mylist)
print("length of list is ", len(mylist))
mylist.sort()
print("sorted list",mylist)
mylist.reverse() #mylist=mylist.reverse()
print("reverse list",mylist)
print("Duplicate item 3",mylist.count(3))
print("Duplicate item 2",mylist.count(2))
