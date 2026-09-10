#Q11

year=int(input("Enter a year:"))

if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
    print("It is a leap Year!!!!")

else:
    print("It's not a leap Year.")

#Q12

#Q13
inn=input("Enter alphabets:").strip().lower()

if inn == "a" or inn == "e" or inn=="o" or inn=="u" or inn=="i":
    print("It's a vowel")
elif inn=="b" or inn=="c" or inn=="d" or inn=="f" or inn=="g" or inn=="h" or inn=="j" or inn=="k" or inn=="l" or inn=="m" or inn=="n" or inn=="p" or inn=="q" or inn=="r" or inn=="s" or inn=="t" or inn=="v" or inn=="w" or inn=="x" or inn=="y" or inn=="z":
    print("It's a consonant")
else:
    print("Invalid Input")

#Q14

cost=int(input("Enter the cost of Product:"))
sell=int(input("Enter the selling price of product:"))

if (cost-sell)>0:
    print(f"It's a Loss of {cost-sell}")
elif (sell-cost)>0:
    print(f"It's a Profit of {sell-cost}")
elif (sell-cost)==0:
    print("No profit and no loss")
else:
    print("Invalid Input")

#Q15

Cost=int(input("Enter the cost of your product:"))
Sell=int(input("Now Selling price of your product:"))
profit=Sell-Cost
loss=Cost-Sell

if Cost<=0:
    print("Invalid Cost Price")
elif (Sell-Cost)>0:
    print(f"It's a profit of {profit} and it's percentage is {(profit/Cost)*100}")
elif (Cost-Sell)>0:
    print(f"It's a loss of {loss} and it's percentage is {(loss/Cost)*100}")
else:
    print("Don't Try to play a game with me")

#Q16 

bill=int(input("Enter the units of your bill:"))

if bill<=100:
    print(f"Your toatl bill is ₹{bill*5}")
elif bill<=200:
    print(f"Your total of bill is ₹{(500)+((bill-100)*7)}")
elif bill>200:
    print(f"Your total of bill is ₹{(1200)+((bill-200)*10)}")

#Q17
fnum=int(input("Enter first number:"))
snum=int(input("Enter second number:"))
op=int(input("Enter 1 for Addition\nEnter 2 for Substraction\nEnter 3 for Multiplication\nEnter 4 for Division:"))
if snum==0:
    print("Second Number cannot be zero")
elif op==1:
    print(f"Addition is {fnum+snum}")
elif op==2:
    print(f"Substraction is {fnum-snum}")
elif op==3:
    print(f"Multiplication is {fnum*snum}")
elif op==4:
    print(f"Division is {fnum/snum}")
else:
    print(f"Invalid input")


#Q18
t=int(input("Enter temperature in celsius:"))

if t<0:
    print("freezing")
elif t<=15:
    print("Very cold")
elif t<=25:
    print("Cold")
elif t<=35:
    print("Normal")
elif t>35:
    print("Hot")

#Q19
N=int(input("Enter a number:"))

if N<0:
    print("It's a negative number")
elif N<=10:
    print("Number is in betweem 0-10")
elif N<=50:
    print("Number is in betweem 11-50")
elif N<=100:
    print("Number is in between 51-100")
elif N>100:
    print("Number is above 100")

# #Q20

A=int(input("Enter the length of 1st side of triangle:"))
B=int(input("Enter the length of 2nd side of triangle:"))
C=int(input("Enter the length of 3rd side of triangle:"))

if (A+B>C) and (A+C>B) and (B+C>A):
    print("These lengths can form a Valid Triangle")
else:
    print("These lengths can't form a Valid Triangle")

    