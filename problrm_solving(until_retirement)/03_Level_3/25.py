number = int(input("Enter a number:"))
str = str(number)
i = 0
i = int(i)
j = len(str) - 1
flag = False

while i<j:
    if str[i] == str[j]:
        i += 1
        j -= 1
        flag = True
    else :
        i += 1
        j -= 1
        flag = False
if flag:
    print("Entered number is a palindrome number")
else:
    print("Entered number is not a palindrome number")