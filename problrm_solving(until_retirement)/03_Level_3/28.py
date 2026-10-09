n = int(input("Enter a number to which you want the fibonacci numbers: "))

a = 0
b = 1
count = 0

while count < n:
    print(a, end=" ")

    next_number = a + b 
    a = b
    b = next_number
    count += 1