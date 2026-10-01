n = int(input("Enter a number: "))

prime = True

for i in range(2,n):
    if n % i == 0:
        prime = False

if prime:
    print(n,"is a prime number")
else :
    print("Not a Prime number")