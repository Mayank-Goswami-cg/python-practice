num = int(input("Enter first number:"))
num1 = int(input("Enter second number:"))
num2 = int(input("Enter third number:"))


if num>num1 & num>num2:
    print(num,"is the greatest one")
elif num1>num & num1>num2:
    print(num1,"is the greatest one")
elif num2>num & num2>num1 :
    print(num2,"is the greatest one")
else :
    print("Invalid input")