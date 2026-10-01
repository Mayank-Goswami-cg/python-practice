n = int(input("Enter a number:"))

for i in range(3,n+1):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False

    if prime:
        print(i,end=" ")
    