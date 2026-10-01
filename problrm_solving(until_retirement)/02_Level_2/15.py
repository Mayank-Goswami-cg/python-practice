number = int(input("Enter the numbers to which you want it's sum:"))
sum = 0
for i in range(1,number+1):
    sum += i
print("Sum of number from 1 to ",number,"is :",sum)