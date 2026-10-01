number = int(input("Enter a number:"))

if number%3 == 0 and number %5 == 0:
    print("Divisible by both 3 and 5")
elif number %3 != 0 and number %5 == 0:
    print("Divisible by 5 but not by 3")
elif number %3 ==0 and number %5 != 0:
    print("Divisible by 3 but not by 5")
elif number %3 != 0 and number %5 != 0:
    print("Not Divisible by both 3 and 5")
else :
    print("Invalid input")