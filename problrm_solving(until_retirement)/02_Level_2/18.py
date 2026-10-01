number = int(input("Enter a number:"))
count = 0 
for i in range(1,number):
    if i%3 == 0:
        count += 1
print(count)