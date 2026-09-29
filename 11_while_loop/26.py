r=int(input("Enter number of rows:"))
c=int(input("Enter number of columns:"))
row = 0
while row < r:
    column = 0
    while column < c:
        print("* ", end="")
        column += 1
    print()
    row += 1