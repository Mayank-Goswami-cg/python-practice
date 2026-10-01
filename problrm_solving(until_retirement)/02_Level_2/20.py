number = int(input("Enter the number of multiples you want of 7: "))
multiple=1
for i in range(1,number+1):
    multiple = 7*i
    print(multiple, end=" ")
print()