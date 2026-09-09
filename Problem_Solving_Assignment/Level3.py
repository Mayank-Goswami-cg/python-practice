#Q21
A=int(input("Enter the length of 1st side of triangle:"))
B=int(input("Enter the length of 2nd side of triangle:"))
C=int(input("Enter the length of 3rd side of triangle:"))


if (A+B>C) and (A+C>B) and (B+C>A):
    print("These lengths can form a Valid Triangle")
elif A+B<C or A+C<B or B+C<A:
    print("These lengths can't form a Valid Triangle")
elif A==B and B==C and A==C:
    print("It's a Equilateral triangle")
elif A==B and B!=C:
    print("It's a Isosceles Triangle")
elif B==C and A!=B:
    print("It's a Isosceles Triangle")
elif A==C and C!=B:
    print("It's a Isosceles")
elif A!=B and B!=C and A!=C:
    print("It's an Scalene Triangle")
 

#Q22

acc=int(input("Enter Account Balance:"))
wid=int(input("Enter The Withdrawal Amount:"))

if wid<=0:
    print("Withdrawal amount must be greater than 0")
elif not wid%100==0:
    print("Withdrawal amount must be in multiple of 100")
elif wid>acc:
    print("Withdrawal amount cannot be greater than account balance")
elif (acc-wid)<500:
    print("Withdrawal Unsuccesfull, After withdrawal atleast ₹500 must remain in Account")
else :
    print(f"Withdrawal Succesful\nRemaining balance: {acc-wid} ")

#Q23
use=input("Enter your username:")
pas=input("Enter your Password:")

if use!="admin":
    print("User not found")
elif pas!="python123":
    print("Wrong Password")
elif use=="admin" and pas=="python123":
    print("Login Succesful")

#Q24
pur=int(input("Enter the purchase amount:"))
di=(pur)-(pur*5/100)
dis=(pur)-(pur*10/100)
disc=(pur)-(pur*15/100)
discount=(pur)-(pur*20/100)

if pur<500:
    print(f"Original Amount:{pur}\nDiscount Percentage 0%\nDiscount Amount 0₹\nFinal Amount {pur}")
elif pur<1000:
    print(f"Original Amount:{pur}\nDiscount Percentage 5%\nDiscount Amount {pur*5/100}\nFinal Amount {di}")
elif pur<2000:
    print(f"Original Amount:{pur}\nDiscount Percentage 10%\nDiscount Amount {pur*10/100}₹\nFinal Amount {dis}")
elif pur<5000:
    print(f"Original Amount:{pur}\nDiscount Percentage 15%\nDiscount Amount {pur*15/100}₹\nFinal Amount {disc}")
elif pur>5000:
    print(f"Original Amount:{pur}\nDiscount Percentage 20%\nDiscount Amount {pur*20/100}₹\nFinal Amount {discount}")

#Q25
m=int(input("Enter your Physics marks:"))
ma=int(input("Enter your chemistry marks:"))
mar=int(input("Enter your MATHEMATICS marks:"))

if m<0 or m>100 or ma<0 or ma>100 or mar<0 or mar>100:
    print("Inappropriate marks please re-enter it!")
elif m<35 or ma<35 or mar<35:
    print("Result: Fail")
elif m>=35 and ma>=35 and mar>=35:
    print("Result: Pass")
    print(f"Your Average marks is {(m+ma+mar)/3}")
    if ((m+ma+mar)/3)>=75:
        print("Distinction")
    elif ((m+ma+mar)/3)>=60:
        print("First Class")
    elif ((m+ma+mar)/3)>=50:
        print("Second Class")
    elif ((m+ma+mar)/3)>=35:
        print("Pass")

#Q26
D=int(input("Enter a date(1-31):"))
DA=int(input("Enter a month(1-12):"))
DAT=int(input("Enter a year(1000-3000):"))

if DA==2:
    if D==29:
        if DAT%400==0 or (DAT%4==0 and DAT%100!=0):
            print(f"{D}/{DA}/{DAT}")
        elif D<29 :
            print(f"{D}/{DA}/{DAT}")
        else :
            print("Invalid Date")
    elif D>=30:
        print("Invalid Date")
elif (D>=31) and (DA==4 or DA==6 or DA==9 or DA==11):
    print("Invalid Date")
elif D>31 or DA>12:
    print("Invalid Date")
else :
    print(f"{D}/{DA}/{DAT}")

#Q27

h=int(input("Enter Hour:"))
m=int(input("Enter minute:"))
s=int(input("Enter second:"))

if h>=0 and h<=23:
    if m>=0 and m<=59:
        if s>=0 and s<=59:
            print(f"Valid Time: {h}-{m}-{s}")
else:
    print("Invalid Time")

#Q28
person_1,age=map(int,input("Enter The name and age of 1st Person:"))
person_2,Age=map(int,input("Enter The name and age of 2nd Person:"))
person_3,AGe=map(int,input("Enter The name and age of 3rd Person:"))

if age>Age and age>AGe:
    print(f"{person_1} is the eldest")