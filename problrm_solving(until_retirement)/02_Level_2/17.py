number = int(input("Enter a number:"))
product = 1
for i in range(1,2):
    for j in range(1,11):
        product = number * j
        print(product, end=" ")
    print()