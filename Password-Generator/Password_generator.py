import secrets #has a stronger randomness compared to the import random. 
import string 

characters = string.ascii_letters + string.digits + string.punctuation

password = "" #password is currently empty

length= int(input("how long do you want your password: "))

for i in range(length): 
    password = password + secrets.choice(characters) #the choice will come from characters
print("Your new password: " + password) 

