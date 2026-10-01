number = int(input("Enter any digit number:"))
sum = 0
num=str(number)
length=len(num)
digit = 0

for i in range(length):
    digit = number % 10
    sum += digit
    number = number//10
print("Sum of digits is",sum)