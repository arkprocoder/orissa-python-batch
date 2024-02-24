numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)
# Result: evens = [2, 4, 6, 8, 10]


# set comprehensions
alphabet=['a','b','c','d','e','f','g']
alphabets={i for i in alphabet if i!='b'}
print(alphabets)
