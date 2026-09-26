# #Q1.

# for i in range(5):
#     print("Hello")


# #Q2.

# for i in range(10):
#     print(i, end=" ")



# #Q3.

# for i in range(1, 11):
#     print(i, end=" ")



# # 4.

# for i in range(10, 0, -1):
#     print(i, end=" ")



# # 5.
# for i in range(5, 51, 5):
#     print(i, end=" ")


# # 6.

# for i in range(2, 21, 2):
#     print(i, end=" ")



# # 7.

# for i in range(1, 20, 2):
#     print(i, end=" ")



# # 8.

# for i in range(3, 19, 3):
#     print(i, end=" ")



# # 9.

# for i in range(20, 1, -2):
#     print(i, end=" ")



# #Q10.

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     print(i, end=" ")


# #Q11.

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i, end=" ")



# #Q12. 

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(i, end=" ")



# #Q13.

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         print(i, end=" ")



# #Q14. 

# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i, end=" ")


# #Q15.

# n = int(input("Enter n: "))

# count = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count += 1

# print("Count of even numbers:", count)



# #Q16.

# n = int(input("Enter n: "))

# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum:", total)


# # 17.

# n = int(input("Enter n: "))

# total = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total = total + i

# print("Sum of even numbers:", total)


# # 18.

# n = int(input("Enter n: "))

# total = 0

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         total = total + i

# print("Sum of odd numbers:", total)


# # 19. 

# n = int(input("Enter number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# # 20.

# n = int(input("Enter n: "))

# result = 1

# for i in range(1, n + 1):
#     result = result * i

# print("Factorial:", result)

# # 21. 

# text = input("Enter a string: ")

# for character in text:
#     print(character)


# # 22. 

# text = input("Enter a string: ")

# for character in text:
#     print(character, end="")



# # 23. 

# text = input("Enter a string: ")

# count = 0

# for character in text:
#     count = count + 1

# print("Number of characters:", count)


# # 24.

# text = input("Enter a string: ")

# count = 0

# for character in text:
#     if character == "a":
#         count = count + 1

# print("Number of a:", count)


# # 25. 

# text = input("Enter a string: ")

# count = 0

# for character in text:
#     if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         count = count + 1

# print("Uppercase characters:", count)

# for i in range(3):
#     for j in range(2):
#         print(i,j)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()

# for i in range(1,6):
#     for j in range(1,7-i):
#         print("*", end="")
#     for k in range(1,i+1):
#         print(" ", end="")
#     print()

num=int(input("Enter row value:"))
for i in range(1,num):
    for j in range(1,num-i,):
        print("*",end="")
    for k in range(1,i+1):
        print(" ",end="")
    print()

# for i in range(1,num):
#     for j in range(1,num-i,):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print()