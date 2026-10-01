number = int(input("Enter the numbers to which you want it's product:"))
product = 1
for i in range(1,number+1):
    product *= i
print("Product of number from 1 to ",number,"is :",product)