import secrets #has a stronger randomness compared to the import random. 
import string 
characters = ""

password = "" #password is currently empty

length= int(input("how long do you want your password: "))
print("Y/N answers only.")
letters = str(input("Do you want letters? "))
digits = str(input("Do you want digits? "))
punctuation = str(input("Do you wants punctuation? "))

if(letters == "Y"): 
    characters = characters + string.ascii_letters#these are all the letters in lower and upper case 
    
if(digits == "Y"): 
    characters = characters + string.digits
    
if(punctuation == "Y"): 
    characters = characters + string.punctuation


for i in range(length): #python for loop  
    password = password + secrets.choice(characters) #the choice will come from characters
print("Your new password: " + password) 

