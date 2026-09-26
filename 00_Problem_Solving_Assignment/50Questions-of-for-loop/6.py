# 6. Number-String Conversion Challenge
# Take 5 numbers from the user.

# For each number:

# Convert it to a string.
# Examine every digit using a loop.
# Count even and odd digits.
# Print which type occurs more.
# If equal, print "Equal".


for i in range(5):
    ct_even=0
    ct_odd=0
    Num=int(input("Enter a number: "))
    Str=str(Num)
    for char in Str:
        j=int(char)
        if(j%2==0):
            ct_even+=1
        else:
            ct_odd+=1
    if(ct_even>ct_odd):
        print("Even digits occur more")
    elif(ct_even<ct_odd):
        print("Odd digits occur more")
    else:
        print("Equal")



