# # Printing table of n using while loop
# i=1
# n=int(input("Enter the number who's table you want:"))
# while i <= 10:
#     print(n, "x",i,"=",i*n)
#     i += 1

# #Q1
# i=1
# while i<=3:
#     print("* "*3)
#     i +=1

# #Q2
# for i in range(1,4):
#     while i<=3:
#         print(i , i+1 , i+2 )
#         i +=1

# password=input("Enter your password:")

# while password != "mayank138080":
#     print("Entered password is:",password)
#     password = input("Entered password is incorrect please try again:")

# print("Correct password!")

# str=input("Enter a string:").lower()
# index=0
# while index < len(str):
#     print(str[index])
    
#     rts=str[::-1]
#     if str[index] == rts[index]:
#         print("Entered string is palindrome")
#     else:
#         print("Entered string is not palindrome")
#         str=input("Again enter a string: ")
#     index += 1


# str1 = input("Enter a string")
# rstr= ""
# i = len(str1) - 1
# while i >= 0:
#     rstr+=str1[i]
#     i -= 1
# if str1 == rstr:
#     print("")


str = input("Enter a string: ").lower()
flag=False
i = 0
j = len(str) - 1

while i<j:
    if str[i] == str[j]:
        i += 1
        j -= 1
        flag=True
    elif str[i] != str[j] :
        i += 1
        j -= 1
        flag=False

if flag==True:
    print("It's a palindrome string")
elif flag==False:
    print("It's not a palindrome string")

# number=int(input("Enter a number:"))

# total = 0

# while number > 0:
#     digit = number % 10
#     total += digit
#     number //= 10

# print("Sum:", total)

row = 1
rows=int(input("Enter the number of rows: "))
while row <= rows:
    column = 1

    while column <= rows:
        if column<=row:
            print("*", end="")
        column = column + 1

    print()
    row = row + 1
