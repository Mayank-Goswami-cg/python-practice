
# i=int(input("ENTER A THREE DIGIT NUMBER:"))
# one=i//10
# two=one//10
# print(f"Sum of digits is: {i%10 + one%10 + two%10}")
# num=int(input("Enter a number:"))
# for i in range(num,num+11):
#     if i%2==0:
#         print(f"{i} is even !!!!!!!")

# str=input("Enter a string:").strip().lower()
# str2=""
# length=len(str)
# for j in range(length-1,-1,-1):
#     str2=str2+str[j]
# if str==str2:
#         print(f"{str} is a Palindrome String")
# elif str!=str2:
#         print(f"{str} is not a Palindrome String")

# rows = 3

# for row in range(1, rows + 1):
#     # Print spaces to center/align the stars
#     for space in range(rows - row):
#         print(" ", end="")
        
#     # Print the odd number of stars (1, 3, 5)
#     for star in range(2 * row - 1):
#         print("*", end="")
        
#     # Move to the next line
#     print()

n=int(input("Enter number of rows:"))
if n%2==0 and n>0:
    for col in range(1,n+1):
        for row in range(1,n+1):
            if row==1 or row==n:
                print("* ",end="")
            elif row==n/2:
                print(" *",end="")
            else :
                print("  ",end="")
        print()
        if col==n:
            print("* "*n)
elif n%2!=0 and n > 0:
    for col in range(1,n+1):
            for row in range(1,n+1):
                if row==1 or row==n:
                    print("* ",end="")
                elif row==(n//2)+1:
                    print("* ",end="")
                else :
                    print("  ",end="")
            print()
            if col==n:
                print("* "*n)
else:
    print("Please enter a valid number")