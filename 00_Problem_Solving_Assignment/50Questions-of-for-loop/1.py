text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for i in text:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    elif i.isdigit():
        digits += 1
    elif i == ' ':
        spaces += 1
    else:
        special += 1

print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Special characters: {special}")

if uppercase > lowercase and uppercase > digits and uppercase > spaces and uppercase > special:
    print("Highest count is",uppercase,"which are of Uppercase letters")
elif (lowercase > uppercase) and lowercase > digits and lowercase > spaces and lowercase > special:
    print("Highest count is",lowercase,"which are of Lowercase letters")
elif digits > uppercase and digits > lowercase and digits > spaces and digits > special:
    print("Highest count is",digits,"which are of digits")
elif spaces > lowercase and spaces > uppercase and spaces > digits and spaces > special:
    print("Highest count is",spaces,"which are spaces")
elif special > lowercase and special > digits and special > spaces and special > uppercase:
    print("Highest count is",special,"which are of special letters")
