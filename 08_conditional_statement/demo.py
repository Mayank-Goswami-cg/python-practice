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
