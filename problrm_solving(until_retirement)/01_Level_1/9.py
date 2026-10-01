year = int(input("Enter a number of year:"))

if year%400 == 0 or year%4 == 0:
    print("Leap year")
elif year %400 != 0 or year%4 != 0:
    print("Odd")
else :
    print("Invalid input")