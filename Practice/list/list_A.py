# Create a list of the first 20 positive integers. Print the list.


list1 = []
for item in range(1,21):
  list1.append(item)
  
print(list1)

# Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.

print(list1[0:5])
print(list1[5:15])



# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.


list2= [x*x for x in range(1,11)]
print(list2)


# Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.

list1 = [x for x in range(1,21) if x%2 == 0]
print(list1)

print ("***********************************8")
import random
list3 = [random.randint(1,10) for _ in range(5)]
print(list3)

list3.sort()
print(list3)

list3.sort(reverse=True)
print(list3)

n = len(list3)

for i in range (n):
  for j in range(n-i-1):
    if list3[j] < list3[j+1]:
      list3[j] , list3[j+1] = list3[j+1] , list3[j]
      
print(list3)

modified=(set(list3))


print(list(modified))



# Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.

list4 = [ 
        [1,2,3,4],
        [5,6,7,8],
        [9,8,7,7]
        ]

print(list4)
print(list4[2][3])

