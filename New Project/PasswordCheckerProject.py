# weak - jayPrakash
# good - JayPrakash123
# strong - jay@1234535 , 123!JayPrakash
# The password length should be atleast 8 characters

password = input('Enter your password: \n').strip()
print(f"Your password is {password}")

# special character - !@#$%^&*
specialCharacter = [] 

# numerics - 1234567890

numerics = []

# alphabetsChars - abc.....

alphabetsChars = []

for i in range(len(password)):
# special chars
    if(not password[i].isalnum()):
        specialCharacter.append(password[i])
#numerics
    if(password[i].isnumeric()):
        numerics.append(password[i])

    if(password[i].isalnum() and ( not password[i].isnumeric())):
        alphabetsChars.append(password[i])
    
    
if(len(password)<8):
    print('Your password should be atleast 8 charaacters')
    
#for strong password...
elif((len(specialCharacter) != 0) and (len(numerics) != 0) and (len(alphabetsChars)!=0)):
    print('Your password is strong')

#for good password...
elif((len(specialCharacter) == 0) and (len(numerics) != 0) and (len(alphabetsChars)!=0)):
    print('Your password is good')

#for strong password...
elif((len(specialCharacter) == 0) and (len(numerics) == 0) and (len(alphabetsChars)!=0)):
    print('Your password is weak')