#password generator
import string
import random
print("It is extremely important to have a safe and secure password")
print("Therefore we will help you keep your data safe by providing a unique sttrong password to keep your data safe")
 #length of the password
length = int(input("Enter password length: "))
 
print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
characterList = ""
 
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
       #adding
        characterList += string.ascii_letters
    elif(choice == 2):
         
        
        characterList += string.digits
    elif(choice == 3):
         
        
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    
    randomchar = random.choice(characterList)
     
    
    password.append(randomchar)
 

print("The random password is " + "".join(password))
print("Thank you for trusting us to choose a unique strong password for you.....🙌")
