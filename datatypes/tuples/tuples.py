empty_tuple = ()
print(empty_tuple)
type(empty_tuple)

# convert list to tuple
# numbers =([1,2,3,4,5])
numbers =tuple([1,2,3,4,5])
print(type(numbers))

# similar to the list we can able to create the mixed tuple 
mixed_tuple = ("Hi", 1, 3.24, True)
print(mixed_tuple)

# Accessing the tuples 
# indexing will be as similar as list 
print(numbers)
print(numbers[0])

# Tuple operations

# concatination 
print(numbers + mixed_tuple)
# (1, 2, 3, 4, 5, 'Hi', 1, 3.24, True)

print(mixed_tuple*3)
# ('Hi', 1, 3.24, True, 'Hi', 1, 3.24, True, 'Hi', 1, 3.24, True)

# Tuple Methods 
print(numbers.count(1))
print(numbers.index(5))

# Packing and Unpacking Tuple 

# Packing 
packed_tuple = 1, "Hello" , 3.14
print(packed_tuple)
# (1, 'Hello', 3.14)

# unpacking 
a,b,c = packed_tuple
print(a,b,c)

# unpacking with *

first,*middle,last = numbers
print(first)
print(middle)
print(last)

# 1
# [2, 3, 4]
# 5

# Nested Tuples 
lst = [[1,2,3,4,5],[1, "Hello" , 3.14],[6,7,8]] # nested list 

nesttuple = ((1,2,3), (True,False),(1, "Hello" , 3.14) )
print(nesttuple[2][1])
print(nesttuple[0][0:4])


# iteration in tuples
for sub_tuple in nesttuple:
  for item in sub_tuple:
    print(item,end=" ")
  print()