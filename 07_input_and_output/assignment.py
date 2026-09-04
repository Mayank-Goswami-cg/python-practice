name = input("Enter your Name:")
print(name)

#Q2
city = input("Enter your city's name:")
print(f"Your city is {city}")

#Q3
your_name=input("Enter your name:")
age= input("Enter your Age:")
print(your_name, age)

#Q4
#What type of value does input() return by default?
#input() returns the value written inside the parenthisis by default

#Q5
value=input("Enter your total marks:")
print(value,type(value))

#Q6
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
print(first_name,last_name)

#Q7
namee=input("Enter your FullName")
cityy=input("Enter your city name:")
collage=input("Enter your Collage name:")
print(f"Your name is {namee} and you are from {cityy}, studying in {collage}")

#Q8
first, second=input("Enter your first and last name").split()

#Q9
# #Suppose the user enters:

# Python Programming
# using one input() statement with .split().

# What values will the two variables receive?
#THE answer will be in list form of ["Python", "Programming"]

#Q10
naam,Age,Gender=input("Enter your name,Age,Gender:")

#Q11 convert the string "25 " into an integer
string="25"
str_int=int(string)

#Q12
stringg="25.5"
str_flt=float(stringg)

#Q13
integer=100
int_str=str(integer)

#Q14
integerr=input("Enter an integer")
print(type(integerr))

#Q15
floatt=input("Enter a floating point")
print(type(floatt))

#Q16
#Why does this produce string concatenation instead of numeric addition?

# a = input()
# b = input()

# print(a + b)

#This is because of input function. if user enters a number in input but thenalso its data type will be string because of which this produces string concatenation

#Q17 Correct the following program so that it performs numeric addition:

# a = input("Enter first number: ")
# b = input("Enter second number: ")

# print(a + b)

a=int(input("Enter first number"))
b=int(input("Enter second number"))

print(a+b)

#Q18
Name="Rahul"
agee="20"
print(f"My name is {Name} and I am {agee} years old")


#Q19
A=10
B=20
print(f"Sum {a+b}")

#Q20
nname=input("Enter your FullName")
Agee=input("Enter your Age")
print(f"Hey there!, My name is {nname} and I am {Agee} years old")

#Q21
product_price=float(input("Enter the price of product in float type:"))
print(f"{product_price:.2f}")

#Q22 What is the purpose of:

# :.2f
# inside an f-string?
#It is used to display 2 digits after the decimal point if we run :.5f then it will display 5 digits after decimal.

#Q23
Product_name=input("Enter your product's name:")
Product_price=int(input("Enter the price:"))
Product_quantity=int(input("Enter the quantity of products"))
print(f"The product is {Product_name} and it's price is decided to be {Product_price} and it's quantity is {Product_quantity}")

#Q24
#What will this display print("A", "B", "C")
#Output A B C 
print("X", "Y", "Z")

#Q25
#Rewrite the following so that the values are separated by -:

print("2026", "08", "19", sep="/")

#Q26
print("Hello", end=" ")
print("World")

#Q27

first_num=int(input("Enter first number:"))
second_num=int(input("Enter second number:"))
print(f"Sum: {first_num + second_num}")

#Q28
Product_name=input("Enter your product's name:")
Product_price=int(input("Enter the price:"))
Product_quantity=int(input("Enter the quantity of products"))
print(f"Total: {Product_price * Product_quantity}")

#Q29
Student_name=input("Enter your name:")
Student_age=int(input("Enter your Age:"))
Student_marks=float(input("Enter your marks"))
print(f"Student's name is {Student_name} and his/her age is {Student_age}.He/She has got {Student_marks} marks.")

#Q30
student_name=input("Enter your name:")
student_age=int(input("Enter your age:"))
student_height=float(input("Enter your height:"))
student_city=input("Enter your city name:")
print(f"Student's name is {student_name} and he/she is {student_age} years old with {student_height:.2f} height")

#Q25
date=int(input("Enter today's date:"))
month=int(input("Month:"))
year=int(input("Year:"))
print(date, month, year, sep="/")