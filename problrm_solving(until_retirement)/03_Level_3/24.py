number = int(input("Enter a number:"))
reverse = 0 
num = str(number)
length = len(num)
digit = 0

for i in range(length):
    digit = number %10
    reverse = reverse*10 + digit
    number = number // 10

print("Reverse of the given number is",reverse)