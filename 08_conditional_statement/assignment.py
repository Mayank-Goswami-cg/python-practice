#Q1
num=int(input("Enter a number:"))

if num>10:
    print("The given number is greater than 10")

#Q2
age=int(input("Enter your age:"))

if age>=18:
    print("Adult")

#Q3
Num=int(input("Enter a number (+ or -) :"))

if Num>0:
    print("Positive")

#Q4
mark=int("Enter your marks:")

if mark>=40:
    print("Pass")

#Q5
nums=int(input("Enter a Number:"))

if num==0:
    print("Zero")

#Q6
Nums=int(input("Enter a Number:"))

if Nums>0:
    print("Positive")

else:
    print("Not Positive")

#Q7
Age=int(input("Enter your age:"))

if Age>=18:
    print("Adult")

else:
    print("Minor")

#Q8
number=int(input("Enter a number:"))

if number%2==0:
    print("Even")

else:
    print("Odd")

#Q9
Mark=int(input("Enter your marks:"))

if Mark>=40:
    print("Pass")

else:
    print("Fail")

#Q10
Number1=int(input("Enter 1st number:"))
Number2=int(input("Enter 2nd number:"))

if Number1>Number2:
    print(f"Greater number is {Number1}")

else:
    print(f"Greater number is {Number2}")

#Q11
marks=int(input("Enter your marks:"))

if marks>90:
    print("A")

elif marks>74:
    print("B")

elif marks>59:
    print("C")

elif marks>39:
    print("D")

else:
    print("F")

#Q12
Number=int(input("Enter a number (+, - or 0):"))

if Number>0:
    print("Positive")

elif Number<0:
    print("Negative")

else:
    print("Zero")

#Q13
Day=input("Enter a number from 1 to 5:")

if Day == 1:
    print("Monday")

elif Day == 2:
    print("Tuesday")

elif Day == 3:
    print("Wednesday")

elif Day == 4:
    print("Thursday")

elif Day == 5:
    print("Friday")

else :
    print("other")

#Q14
Marks=int(input("Enter your marks"))

if Marks>=90:
    print("Excellent")

elif Marks>=70:
    print("Good")

elif Marks>=40:
    print("Pass")

else :
    print("Fail")

#Q15
nume=int(input("Enter a number from 1 to 3:"))

if nume == 1:
    print("You have chosen 1")

elif nume == 2:
    print("You have chosen 2")

elif nume == 3:
    print("You have chosen 3")

else :
    print("You have chosen a number out of range")

#Q16
Agee=int(input("Enter your age:"))

if Agee>= 18:
    if Agee<60:
        print("Age is between 18 and 60")

    else :
        print("Age is above 60")

else :
    print("Age is below 18")

#Q17
markss=int(input("Enter your marks:"))

if markss>=40:
    if markss>=75:
        print("Good")

    else :
        print("Passed")

else :
    print("Failed")

#Q18

Nume=int(input("Enter a Number:"))

if Nume >= 0:
    if Nume >= 100:
        print("The given Number is positive and Above 100")

    else :
        print("The Given Number Is Positive but below 100")


else :
    print("Provided number is Negative")

#Q19

agee=int(input("Enter your age:"))

if agee >= 18:
    if agee <= 60:
        print("Provided age is in between 18 and 60")

    else :
        print("Provided age is above 60")

else :
    print("Provided age is below 18")

#Q20
Numberr=int(input("Enter any number:"))

if Numberr != 0:
    if Numberr > 0:
        print("Provided number is Positive")

    else :
        print("Provided number is Negative")

else :
    print("Provided number is 0")

#Q21
MARK=int(input("Enter your marks:"))
AGE=int(input("Enter your age:"))

if AGE >= 18:
    if MARK >= 40:
        print("Eligible")

else :
    print("Not eligible")

#Q22
NUMBER=int(input("Enter any number:"))

if NUMBER < 10:
    if NUMBER > 100:
        print("Special")

else :
    print("Common")

#Q23
AGEE=int(input("Enter your age:"))
id=bool(input("has_id if yes then type 1 else type 0:"))

if AGEE>= 18:
    if id == True:
        print("Allowed")

else :
    print("Not Allowed")

#Q24
number1=int(input("Enter 1st number:"))
number2=int(input("Enter 2nd number:"))

if number1 > 10:
    if number2 > 10:
        print("Both numbers are greater than 10")
else :
    print("One of the two number is not Greater than 10")

#Q25
numb=int(input("Enter a number:"))

if numb < 0:
    if numb > 100:
        print("Number is greater than 100")

    else :
        print("Number is less than 100")
a="18"
b=18

print(a >= b)
