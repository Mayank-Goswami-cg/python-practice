# 31


# Problem 1
# Print numbers from 1 to 10, but stop when the number becomes 6.
# i = 1
# while i <=10:
#     if i == 6:
#         break
#     print(i)
#     i+=1

# Problem 2
# Given:

# numbers = [10, 20, 30, 40, 50]
# Search for 30.

# Once found, print:

# Found
# and stop the loop.

# numbers = [10, 20, 30, 40, 50]
# l = len(numbers)
# i = 0 
# while i<=l:
#     if numbers[i] == 30:
#         print("Found")
#         break

#     i+=1


# Problem 3
# Take numbers from the user continuously.

# Stop when the user enters 0.

# i = 0
# num = 1
# while i<=num:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         print("Loop Stopped")
#         break
    

# Problem 4
# Print numbers from 1 to 100, but stop when you reach the first number divisible by 17.

# i = 1
# while i<=100:
#     if i%17 ==0:
#         break
#     print(i)
#     i+=1


# 32

# for i in range(1,21):
#     if i % 2 == 0:
#         i+=1
#         continue
#     print(i)
#     i+=1


# numbers = [10, -2, 30, -5, 40, -8]
# l = len(numbers)
# for i in range(0,l):
#     if numbers[i]>0:
#         print(numbers[i])


# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i, end=" ")


# number = [5, 12, 8, 21, 30, 7]
# le = len(number)
# for i in range(0,le):
#     if number[i]<10:
#         continue
#     print(number[i])

# for i in range(1, 6):
#     if i == 3:
#         pass

#     print(i)






# Mixed Questions

#Q1


for i in range(1, 6):
    if i == 3:
        break

    print(i)
# 1,2


#Q2

for i in range(1, 6):
    if i == 3:
        continue

    print(i)
# 1, 2, 4, 5.


#Q3

for i in range(1, 6):
    if i == 3:
        pass

    print(i)
# 1, 2, 3, 4, 5.


#Q4

i = 1

while i <= 5:
    if i == 3:
        continue

    print(i)
    i += 1
# 1, 2, infinite loop


#Q5

for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break

    print(i)
# 1, 2.


#Q6

for i in range(1, 6):
    if i == 3:
        break
else:
    print("Done")
#1, 2.


#Q7

for i in range(1, 6):
    if i == 3:
        continue
else:
    print("Done")
# Done.

for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")