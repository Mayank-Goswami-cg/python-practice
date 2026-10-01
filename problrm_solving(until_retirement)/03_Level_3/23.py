number = int(input("Enter any digit number:"))
product = 1
num=str(number)
length=len(num)
digit = 0

for i in range(length):
    digit = number % 10
    product *= digit
    number = number//10
print("Product of digits is",product)