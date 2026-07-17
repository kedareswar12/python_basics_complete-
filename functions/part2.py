# temperature convertion 
def temp_convertion(temp,unit):
  """This will convert celcius to fahrenheit """
  if unit=='C':
    return temp * 9/5 +32
  elif unit=="F":
    return(temp-32)*5/9
  else:
    return None
  
print(temp_convertion(32,'C'))

# Password strength checker 
def strong_password(password):
  if len(password)< 8:
    return False 
  if not any(char.isdigit() for char in password):
    return False 