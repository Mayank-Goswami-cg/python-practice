# 1

num = int(input("Enter Marks :-"))
if 0 <= num <= 100:
    print("valid number")
else:
    print("INVALID NUMBER")
    num = int(input("Enter Marks :-"))

# 2

num = int(input("Enter an integer greater than 0: "))

while num <= 0:
    num = int(input("Invalid number! Enter again: "))

print("Accepted number:", num)

# 3

age = int(input("Enter your age: "))

while age < 0 or age > 120:
    print("Error! Age must be between 0 and 120.")
    age = int(input("Enter your age again: "))

print("Accepted age:", age)

# 4


choice = int(input("Enter your choice (1-4): "))

while choice < 1 and choice > 4:
    print("Invalid choice! Please enter 1, 2, 3, or 4.")

    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Selected option: View profile")
elif choice == 2:
    print("Selected option: Edit profile")
elif choice == 3:
    print("Selected option: Settings")
else:
    print("Selected option: Exit")

# 5

password = input("Enter your password: ")

while len(password.strip()) < 8:
    print("Password must contain at least 8 characters.")
    password = input("Enter your password: ")

print("Password accepted successfully!")

# 6

temperature = int(input("Enter temperature between -20 and 45: "))

while temperature < -20 or temperature > 45:
    print("Invalid temperature! Try again.")
    temperature = int(input("Enter temperature between -20 and 45: "))

print("Valid temperature:", temperature)

# 7

balance = 5000

amount = int(input("Enter withdrawal amount: ₹"))

while amount <= 0 or amount > balance:
    print("Invalid amount! Please try again.")
    amount = int(input("Enter withdrawal amount: ₹"))

balance = balance - amount

print("Withdrawal successful!")
print("Remaining balance: ₹", balance)

# 8

username = input("Enter username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid username! Try again.")
    username = input("Enter username: ").strip()

print("Accepted username:", username)

# 9

num = int(input("Enter a positive integer divisible by 3 and 5: "))

while num <= 0 or num % 3 != 0 or num % 5 != 0:
    print("Invalid number! Try again.")
    num = int(input("Enter a positive integer divisible by 3 and 5: "))

print("Accepted number:", num)

# 10

secret_pin = 2468
attempts = 0
while attempts < 3:
    pin = int(input("Enter your PIN: "))
    if pin == secret_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN!")
        attempts = attempts + 1
if attempts == 3:
    print("Access denied!")

# 11

num = int(input("Enter an integer between 10 and 50: "))
while num < 10 or num > 50:
    print("Invalid number! Try again.")
    num = int(input("Enter an integer between 10 and 50: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 12

balance = 2000
deposit = int(input("Enter deposit amount: ₹"))
while deposit <= 0:
    print("Invalid amount! Deposit must be positive.")
    deposit = int(input("Enter deposit amount: ₹"))
balance = balance + deposit
print("New balance: ₹", balance)

# 13

num = int(input("Enter an integer between 1 and 100: "))
while num < 1 or num > 100:
    print("Invalid number! Try again.")
    num = int(input("Enter an integer between 1 and 100: "))
print("Accepted number:", num)

# 14

marks = int(input("Enter marks between 0 and 100: "))

while marks < 0 or marks > 100:
    print("Invalid marks! Try again.")
    marks = int(input("Enter marks between 0 and 100: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")

# 15

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    username = username.strip()
    password = password.strip()
    if len(username) >= 5 and " " not in username and len(password) >= 8:
        print("Username and password are valid!")
        break
    else:
        print("Invalid username or password. Try again.")

# 16

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operator! Try again.")
    operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
while operator == "/" and num2 == 0:
    print("Division by zero is not allowed!")
    num2 = float(input("Enter second number again: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
else:
    result = num1 / num2
print("Result:", result)

# 17


balance = 10000

choice = 0

while choice != 4:
    print("\n--- Banking Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is ₹", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Updated balance: ₹", balance)
        else:
            print("Deposit amount must be greater than zero.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Updated balance: ₹", balance)

    elif choice == 4:
        print("Thank you for using our banking system!")

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

# 18


month = int(input("enter month:-"))
day  = int(input("enter day:-"))
while month < 1 or month > 12 or day < 1 or day > 31:
    print("invalid")
    month = int(input("enter month:-"))
    day  = int(input("enter day:-"))
print("Valid month:",month)
print("Valid day:",day)


# 19

quanitity = int(input("enter product quanitity:-"))
price = int(input("enter price of product:-"))

while quanitity < 0 or price <0:
    print("invalid")
    quanitity = int(input("enter product quanitity:-"))
    price = int(input("enter price of product:-"))

print("product qyanitity :-" , quanitity)
price("price :- ", price)
price("total money :- ",price*quanitity)

# 20

total = 0
n = int(input("how many numbers you want to enter:-"))
p = n
while n>0:
    num = int(input("enter your number:-"))
    while num >20 or num < 0:
        print("invalid")
        num = int(input("enter your number again:-"))
    total += num
    n-=1
print("avrage of all number :- ", total/p)

# 21


password = input("Enter your password: ")

while True:
    length_ok = len(password) >= 8
    upper_ok = False
    lower_ok = False
    digit_ok = False
    space_ok = True

    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            upper_ok = True
        elif ch >= 'a' and ch <= 'z':
            lower_ok = True
        elif ch >= '0' and ch <= '9':
            digit_ok = True

        if ch.isspace():
            space_ok = False

    if length_ok and upper_ok and lower_ok and digit_ok and space_ok:
        print("Password accepted!")
        break

    print("Password does not meet these rules:")

    if not length_ok:
        print("- At least 8 characters are required.")
    if not upper_ok:
        print("- At least one uppercase letter is required.")
    if not lower_ok:
        print("- At least one lowercase letter is required.")
    if not digit_ok:
        print("- At least one digit is required.")
    if not space_ok:
        print("- Whitespace characters are not allowed.")

    password = input("Enter your password again: ")

# 22

n = int(input("enter you number (1-10):-"))
while n <0 or n > 10:
    print("invalid number:-")
    n = int(input("enter you number (1-10) :-"))
print("valid number")

# 23


total = 0
for i in range(3):
    score = int(input("enter score :-"))
    while score >100 or score < 0:
        print("invalid score")
        score = int(input("enter score again :-"))
    total += score
print("total score :-",total)
print("avg score :-",total/3)
    
# 24

balance = 10000
amount = int(input("Enter withdrawal amount: ₹"))
while amount <= 0 or amount > balance or amount % 100 != 0:
    print("Invalid withdrawal amount!")
    if amount <= 0:
        print("Amount must be greater than zero.")
    elif amount > balance:
        print("Amount must not exceed your balance.")
    elif amount % 100 != 0:
        print("Amount must be a multiple of ₹100.")
    amount = int(input("Enter withdrawal amount again: ₹"))
balance = balance - amount
print("Withdrawn amount: ₹", amount)
print("Remaining balance: ₹", balance)