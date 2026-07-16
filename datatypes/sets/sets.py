# used to store the collection of the unique items 
# -> unordered = they dont follow any order and dont allo duplicates 


# create a set
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

print(list(my_set))

new_set ={1,2,3,4,5,6,3,2,4}
print(new_set)
# output -> {1, 2, 3, 4, 5, 6}

# Basic set opetarions 

#Adding and removing the elements 
print(my_set)
my_set.add(6)
print(my_set)

# Reoving the elements from the set
my_set.remove(3)
print(my_set)

# in sets incase of remove if the number is not present in the set then it will raise an error so if not to raise the error then you need to use the discard() method (removing if is a member of the set)

remove_element = my_set.pop()
print(remove_element)
# Follows the FIFO method 

my_set.clear()
print(my_set)

# Set Meber of the set 
my_set = {1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)

# union -> combinig the 2 sets 
# intersection -> common element of the sets 
# differnce -> removes the common elemnts and gives the remaning elements 
#symmetric differnce -> only unique elemnts of  both sets are  printed 

# Set Methods 

set1 ={1,2,3}
set2 ={3,4,5}

# is subset
print(set1.issubset(set2))
print(set1.issuperset(set2))

# ##Count the number of words in the set 

text = "Hi i am kedareswar and learning python"
words = text.split()

print(words) #List format
print(set(words))
print(len(words))
