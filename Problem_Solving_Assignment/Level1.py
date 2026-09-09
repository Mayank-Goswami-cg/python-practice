#Q1
num1=int(input("Enter a number:"))

if num1 > 0:
    print("Positive")
elif num1< 0:
    print("Negative")
elif num1 == 0:
    print("Zero")

else:
    print("Not a number")
#Q2

num2=int(input("Enter a Number:"))

if num2 > 0 and num2%2==0:
    print("Positive Even")
elif num2 >0 and num2%2!=0:
    print("Positive odd")
elif num2<0 and num2%2==0:
    print("Negative Even")
elif num2<0 and num2%2!=0:
    print("Negative Odd")
elif num2==0:
    print("Zero")
else:
    print("Invalid Number")

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))

if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
elif n1 == n2:
    print("Both are equal")
else:
    print("Undefined number entered")

#Q4

nu1=int(input("Enter First Number:"))
nu2=int(input("Enter Second Number:"))
nu3=int(input("Enter Third Number:"))

if nu1<nu2 and nu1<nu3:
    print(nu1)
elif nu2<nu1 and nu2<nu3:
    print(nu2)
elif nu3<nu1 and nu3 < nu2:
    print(nu3)
else:
    print("Not a number entered")

#Q5

nb1=int(input("Enter First Number:"))
nb2=int(input("Enter Second Number:"))
nb3=int(input("Enter Third Number:"))

if nb1>nb2 and nb1>nb3:
    print(nb1)
elif nb2>nb1 and nb2>nb3:
    print(nb2)
elif nb3<nb1 and nb3 < nb2:
    print(nb3)
else:
    print("Not a number entered") 

#Q6

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible only by 5")
elif num % 11 == 0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")

#Q7

number = int(input("Enter a Number:"))

if number % 3 == 0 and number % 7 == 0:
    print("Divisible by both")
elif number % 3 == 0 :
    print("Divisible by only 3")
elif number % 7 == 0:
    print("Divisible by only 7")
else :
    print("Divisible by neither")

#Q8

marks=int(input("Enter your marks:"))

if marks<0 or marks>100:
    print("Invalid marks")

elif marks>=40:
    print("Pass")
elif marks<40:
    print("Fail")
else :
    print("Entered marks are not integer type")

#Q9
mark=int(input("Enter your marks:"))

if mark>=90:
    print("A")
elif mark>=80:
    print("B")
elif mark>=70:
    print("C")
elif mark>=60:
    print("D")
elif mark>=40:
    print("E")
else:
    print("FAIL")

#Q10

age=int(input("Enter your Age:"))

if age<0:
    print("Invalid Age")
elif age<18:
    print("Cannot Vote")
elif age>=18:
    print("Can vote")
elif age>=120:
    print("Unrealistic age entered")


