# Ecxeptions are the error that occur while program is running 
# it they are not stoped then the program will stop the execution 

# num = int("Kedar")

# ValueError
#FileNotFoundError
# ZeroDivisionError
#KeyError
#TypeError 
#IndexError


#Traceback -> shows where the error happend and what type of the error occured 


#try is used to write the riskey code and except handels the error when something goes wrong 


try: # this is the place where error might happen
  num = int(input("Enter your number: "))
  print(num)
except ValueError: # place where the error is handled
  print("Invalud input please type the number")
else:
  print("Successful Conversion : " , num)
finally:
  print("This will always runs")

  # output 
# ➜  exception git:(main) ✗ python3 errors_handling.py
# Enter your number54
# 54
# Successful Conversion :  54
# This will always runs
# ➜  exception git:(main) ✗ python3 errors_handling.py
# Enter your number: Kedar
# Invalud input please type the number
# This will always runs

print("******************* Brod Exception *****************")
# Broad exception 
# try:
#   result =10/0
# except Exception as e:
#   print("Something went wrong" , e)


#   #raise 

#   def withdraw(with_ammount , balance):
#     if with_ammount > balance:
#       raise ValueError("Insufficient balance")
    
#     return balance - with_ammount
    
#   print(withdraw(1500 ,100))

# custom errors -> creates the meaning full errors for our own appliation 

# class InsufficientbalanceError(Exception):
#   pass

# def withdraw(with_ammount , balance):
#     if with_ammount > balance:
#       raise ValueError("Insufficient balance")
    
#     return balance - with_ammount

# try:
#   withdraw(1900,190)
# except InsufficientbalanceError as e:
#   print(e)


# class InsufficientBalanceError(Exception):
#     pass

# def withdraw(withdraw_amount, balance):
#     if withdraw_amount > balance:
#         raise InsufficientBalanceError("Insufficient balance")

#     return balance - withdraw_amount

# try:
#     withdraw(1900, 190)
# except InsufficientBalanceError as e:
#     print(e)


print("******************Exception Chaining************************")
#Exception Chaining 
# -> If one exception happens becaue of the another exception this happens 
def convert_to_int(value):
  try:
    return int(value)
  except ValueError as e:
    raise ValueError("Failed to convert the value from string to integer") from e 

convert_to_int("abc")


# incase of file handling

try:
  file = open('example1.txt' , "r")
  content = file.read()
  print(content)

except FileNotFoundError :
  print("File not exists")

finally:
  if file in locals() or  not file.close():
    file.close()
    print("File is closed successfully")

  
