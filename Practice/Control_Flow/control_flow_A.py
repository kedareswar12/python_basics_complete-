# Write a program that asks the user to input a number and prints whether the number is positive.

number = int(input("Enter your number: "))

if(number !=  0):
  print("positive")
  
  
  
# Write a program that prints all the numbers from 1 to 10 using a for loop.
  
for i in range(1,11):
  print(i)
  
num =1
while (num<=10):
  print(num)
  num = num + 1


# Write a program that prints a 5x5 grid of asterisks (*) using nested loops.

for i in range(1,6):
  for j in range(1,6):
    print ("*",end = " ")
  print()
    
# Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

sum =0

while( True ):
  num = int(input("Enter your number: "))
  sum = sum + num 
  if ( num ==0):
    break

print(sum)
  
# Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.

for i in range(1,11):
  
  if( i ==5 ):
    continue
  print(i)
  
  
# Write a program that calculates the factorial of a number input by the user using a while loop.

fact : int = 1
num :int = int(input("Enter the number : "))
while(num > 0):
  fact = fact * num
  num = num - 1
  
print(fact)  
  
# Write a program that calculates the sum of the digits of a number input by the user using a while loop.

number : int = int(input("Enter the number"))
sum1 =0
while (number > 0)  :
  last_digit = number % 10
  sum1 = sum1 + last_digit
  number //= 10

print(sum1)


# Fibonacci Sequence 
n : int = int(input("Entrt your number: "))

first = 0
second = 1

if num == 0:
  print(first)
elif num == 1:
  print(second)
  
else:
  for i in range(2,n+1):
    next = first + second
    first =second
    second = next 
    
print(second)