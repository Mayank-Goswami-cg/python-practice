# # num=int(input("Enter number of rows:"))

# # for row in range (1,num+1):
# #     for space in range(num-row):
# #         print(" ",end="")
# #     for star in range(2*row-1):
# #         print("*", end="")
# #     print()


# total=0
# flag=True
# grade=" "

# for i in range(5):
#     marks=int(input("Enter marks of different subjects:"))
#     total += marks
#     if marks<35:
#         flag=False

# if flag:
#     percentage=total/5
#     if percentage>=90:
#         grade="A+"
#     elif percentage>=80:
#         grade="A"
#     elif percentage>=70:
#         grade="B"
#     elif percentage>=60:
#         grade="C"
#     elif percentage>=50:
#         grade="D"
#     elif percentage<50:
#         grade="F"
# else:
#     grade="F"

# print("Total :",total,"\nPercentage :",percentage,"\nGrade :",grade)

# if flag:
#     print("Result : Pass!")
# else:
#     print("Result : Fail")

# Number of rows
rows = int(input("Enter number of rows:"))

for i in range(rows):
    if i == rows - 1:
        print((rows)*"* ")
    else:
        print("*",(rows)*" ","*")
