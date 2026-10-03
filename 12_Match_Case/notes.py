# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
# while menu != 0:
#     match menu:
#         case 1:
#             print(f"{num1} + {num2} = {num1 + num2}")
#             menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
#         case 2:
#                 print(f"{num1} - {num2} = {num1 - num2}")
#                 menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
#         case 3:
#                 print(f"{num1} x {num2} = {num1 * num2}")
#                 menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
#         case 4:
#                 print(f"{num1} / {num2} = {num1 / num2}")
#                 menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
#         case 5:
#                 print(f"{num1} // {num2} = {num1 // num2}")
#                 menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
#         case 6:
#                 print(f"{num1} ** {num2} = {num1 ** num2}")
#                 menu=int(input("Which operation do you want to perform?\n0 ==> For exit\n1 ==> Addition\n2 ==> Substraction\n3 ==> Multiplication\n4 ==> Division\n5 ==> Modulus\n6 ==> Exponentiation : "))
#         case _:
#                 print(f"Invalid input")






# menu = 1

# while menu != 0:
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     menu=int(input("Which operation do you want to perform?\n\t0 ==> For exit\n\t1 ==> Addition\n\t2 ==> Substraction\n\t3 ==> Multiplication\n\t4 ==> Division\n\t5 ==> Modulus\n\t6 ==> Exponentiation : "))
           
#     match menu:
#         case 1:
#             print(f"{num1} + {num2} = {num1 + num2}")
                
#         case 2:
#                 print(f"{num1} - {num2} = {num1 - num2}")
                    
#         case 3:
#                 print(f"{num1} x {num2} = {num1 * num2}")
                    
#         case 4:
#                 if num2 != 0:
#                     print(f"{num1} / {num2} = {num1 / num2}")
#                 else :
#                     print("Second Number can't be ZERO")
                    
#         case 5:
#                 print(f"{num1} // {num2} = {num1 // num2}")
                    
#         case 6:
#                 print(f"{num1} ** {num2} = {num1 ** num2}")
                    
#         case 0:
#                 print(f"Exited Successfuly")
#         case _:
#                   print("Invalid Operation!")



# day_number=int(input("Enter the Day Number: "))

# match day_number:
#     case 1 | 2 | 3 | 4 | 5 :
#         print("Weekday")
#     case 6 | 7 :
#         print("Weekend")
#     case _ :
#         print("Invalid Input")


# marks = int(input("Enter your marks: "))

# match marks:
#     case x if x >= 100:
#         print("Invalid input")
#     case x if x >= 90:
#         print("A")
#     case x if x >= 70:
#         print("B")
#     case x if x >= 50:
#         print("C")
#     case x if x >= 35:
#         print("D")
#     case x if x < 0:
#         print("Invalid input")
#     case x if x < 35:
#         print("F")
#     case _ :
#         print("Invalid input")


category = int(input("Enter\n\t1 ==> Student\n\t2 ==> Faculty\n\t3 ==> Managment: "))
match category:
    case 1:
        choice1 = int(input("Enter Your Choice\n\t1 ==> view Profile\n\t2 ==> View TimeTable\n\t3 ==> View Attendance: "))
        match choice1:
            case 1:
                print("Your Profile")
            case 2:
                print("TimeTable")
            case 3:
                print("Your Attendance")
            case _ :
                print("Invalid Input")
    case 2:
        choice2 = int(input("Enter Your Choice\n\t1 ==> Track Attendance\n\t2 ==> Track Students\n\t3 ==> Track Exam Details: "))
        match choice2:
            case 1:
                print("Tracking Attendance")
            case 2:
                print("Tracking Students")
            case 3:
                print("Tracking Exam Details")
            case _ :
                print("Invalid Input")
    case 3:
        choice3 = int(input("Enter Your Choice\n\t1 ==> Track Everything\n\t2 ==> Track Teachers\n\t3 ==> Track Infrastructure: "))
        match choice3:
            case 1:
                print("Tracking Every Details")
            case 2:
                print("tracking Teachers Details")
            case 3:
                print("Tracking Infrastructure Details")
            case _ :
                print("Invalid Input")
    case _ :
        print("Invalid Input")





