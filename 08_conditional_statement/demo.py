# name=input("Enter Your Name:")
# Age=int(input("How old are you?"))

# if Age>=18:
#     print(f"Hey,{name} you are an adult!")
# else:
#     print(f"Hey,{name}You are an minor till now!")

age = int(input("Enter your age:").split()[0])
Gender=input("Enter your gender:")
Gender=Gender.lower().strip()

if age >= 18:
    if Gender=="female":
        print("Seat is available foy youhh!!")

    if Gender!="female":
        print("Seat is not available for you :)")

else :
    print("No seats for minors")


a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("For addition type 1 or\nFor substraction type 2 or\nFor Multiplication type 3 or\nFor division type 4 or\nFor floor division type 5:")

if c=="1":
    print(a + b)
elif c=="2":
    print(a - b)
elif c=="3":
    print(a * b)
elif c =="4":
    print(a/b)
elif c=="5":
    print(a//b)
else:
    print("Invalid value entered")