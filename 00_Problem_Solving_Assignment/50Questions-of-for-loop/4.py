# 4. Password Batch Validator
# Take passwords for 5 users using a for loop.

# For every password, check:

# Minimum length of 8.
# At least one uppercase letter.
# At least one lowercase letter.
# At least one digit.
# At least one special character.
# Print "Strong", "Medium", or "Weak" based on the number of conditions satisfied.


for i in range(5):
    ct_up=0
    ct_lw=0
    ct_spe=0
    ct_dig=0
    count=0
    Pass=input("Enter the password: ")
    if(len(Pass)>=8):
        count+=1
    for char in Pass:
        if(char>='A' and char<='Z'):
            ct_up+=1
        elif(char>='a' and char<='z'):
            ct_lw+=1
        elif(char>='0' and char<='9'):
            ct_dig+=1
        else:
            ct_spe+=1
    if(ct_up>0):
        count+=1
    elif(ct_dig>0):
        count+=1
    elif(ct_lw>0):
        count+=1
    elif(ct_spe>0):
        count+=1
    if(count==5):
        print("Password is strong")
    elif(count>=3):
        print("Password is medium")
    else:
        print("Password is weak")