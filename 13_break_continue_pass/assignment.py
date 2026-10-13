# Section A

# A1

# Q1 for i in range(1, 8):
#     if i == 5:
#         break
#     print(i)
# print("Finished")

# Output 

# 1 2 3 4 Finished (all of them in new lines)

# Q2 
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)

# Output

# s k y l (all of them in new lines)

# Q3 n = 2

while n <= 10:
    print(n)
    if n == 6:
        break
    n += 2

# Output 

# 2 4 6 (in new lines)




# A2 Write a Program

# Q4 . Stop at a Target Number
# Take an integer limit. Print numbers from 1 through limit, but stop before printing 7.

# If limit is less than 7, print all numbers up to limit.

# Test cases

# Input Expected output

# 10 1 2 3 4 5 6 5 1 2 3 4 5 7 1 2 3 4 5 6

# Print the numbers on one line, separated by spaces.

limit = int(input("Enter a Number: "))
i = 1
while i<=limit:
    if i == 7:
        break
    print(i,end = " ")
    i += 1


# Q5 Find the First Matching Character
# Take a string and a target character. Scan the string from left to right. Print each character as it is checked. Stop immediately after finding the target.

# If the target does not appear, check the entire string.

# Test cases

# Input string Target Expected checked characters

# computer p c o m p banana x b a n a n a level l l

string = input("Enter a Word: ").lower()
l = len(string)
i = 0 
while i <= l-1:
    print(string[i], end = " ")
    if string[i] == "o":
        break
    i += 1


# Q6. Stop at a Negative Number
# Given a sequence of integers, print numbers from left to right and stop when the first negative number is encountered. Do not print the negative number.

# Test cases

# Input Expected output

# 4 8 2 -3 9 4 8 2 -1 5 6 No numbers printed 2 4 6 2 4 6

arr = [4, 8, 2, -3, 9]
le = len(arr)
i = 0
while i<=le-1:
    if arr[i]<0:
        break
    print(arr[i], end = " ")
    i+=1


# A3 Think Carefully -- Challenging

# Q7. break Only Exits the Inner Loop
# Predict the output.

for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)
# Explain why the outer loop continues.


# 1 1
# 1 2
# 2 1 
# 2 2
# 3 1
# 3 2
# The outer loop continues because break only terminates the inner loop since it is inside the inner loop

# Q8. Search a Word
# Take a sentence and a target word. Check the words from left to right. Print "Found" and stop when the target word is found. If the target is absent, print "Not found".

# Test cases

# Sentence Target Expected output

# python makes coding fun coding Found loops are useful java Not found learn python python python Found

sentence = input("Enter a Sentence: ")
L = len(sentence)
i = 0
while i <= L-1:
    if sentence[i] == "World":
        print("Found")
    i += 1
else:
    print("Not Found")


# Section B --- Practice Problems on continue

# B1. Output Prediction --- Easy


# Q9. Skip Number 4

# Predict the output.

for i in range(1, 7):
    if i == 4:
        continue
    print(i)

# Output 

# 1 2 3 5 6 (all of them in new lines)

# Q10. Skip Vowels

# Predict the output.

for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")

# Output 

# dctn

# Q11. continue in a while Loop


# Predict the output.

n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

# Output

# 1 2 4 (all of them in new lines)


# B2. Write a Program --- Medium



# Q12. Print Numbers That Are Not Multiples of 3

# Take an integer n. Print numbers from 1 to n, skipping multiples of 3.

# Test cases

# Input Expected output

# 8 1 2 4 5 7 8 3 1 2 2 1 2

n = int(input("Enter a integer: "))
i = 1
while i<=n:
    if i %3 ==0:
        i+=1
        continue
    print(i, end = " ")
    i+=1 


# Q13. Remove a Chosen Character from Display

# Take a string and a character. Print the string without displaying any occurrence of that character. Do not use string replacement methods; use a loop and continue.

# Test cases

# String Character Expected output

# mississippi s miippi banana a bnn hello x hello

STR = input("Enter a Word: ").lower()
LE = len(STR)
i = 0
while i<= LE-1:
    if STR[i] == "s":
        i += 1
        continue
    print(STR[i], end = " ")
    i+=1


# Q14. Print Only Passing Marks


# Given marks separated by spaces, print only marks that are at least 40. Use continue to skip marks below 40.

# Test cases

# Input Expected output

# 25 40 75 32 90 40 75 90 10 20 30 No marks printed 40 40 40 40 40 40

ARR = [25, 40, 75, 32, 90]
LEN = len(ARR)
i = 0
while i<=LEN-1:
    if ARR[i]<35:
        i+=1
        continue
    print(ARR[i], end = " ")
    i += 1


# Q15
for i in range(1, 5):
    if i == 2:
        continue
    print("A", i)
    print("B", i)

# OUTPUT:-
# A 1
# B 1
# A 3
# B 3
# A 4
# B 4


# Q16
n = 0

while n < 5:
    n+=1
    if n == 3:
        
        continue
    
    print(n)


# Q17
str=input("Enter any string:-").strip().lower()
count=0
for i in str:
    if i in "aeiou":
       count+=1
       continue
print(count)  


# Q18
for i in range(1, 4):
    print(i)
else:
    print("Done")

# OUTPUT:-
# 1
# 2
# 3
# Done 


# Q19
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

# OUTPUT:-
# 1
# 3
# 4
# Completed 



# Q20
for i in range(1, 5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
print("Outside loop")


# OUTPUT:-
# 1
# 2
# Outside loop 


# Q21
for item in []:
    print("Inside")
else:
    print("Else block")

# OUTPUT:-
# Else block 



# Q22

num=[12,14,16,18,20]

for i in num:
    if i==12:
        print("Found")
        break
else:
    print("Not found")  


# Q23
str=input("Enter any string:-")
for i in str:
    if i=="a":
        print("Character exists")
        break
else:
    print("Character not found")


# Q24


# Q25
# values = [2, 4, 6, 8]

# for value in values:
#     if value % 2 != 0:
#         print("Odd found")
#         break
# else:
#     print("All are even")

# OUTPUT:- All are even


# Q26
# case 1 
# for x in range(3):
#     continue
# else:
#     print("A")   OUTPUT:- A


# case 2
# for x in range(3):
#     break
# else:
#     print("B")  OUTPUT:- B


# case 3
# for x in range(0):
#     print(x)
# else:
#     print("C")

# OUTPUT:- 
# C

# Q27


s = input("Enter a string: ").lower()


for i in range(len(s)):
    ch = s[i]
    if s.count(ch) >= 2:
        print("Repeated Character is: ",ch)
        break
else:
    print("No repeated character")

word = input("Enter a word: ").lower().strip()

for i in range(len(word)):
    for j in range(i + 1, len(word)):
        if word[i] == word[j]:
            print("Repeated character is:", word[i])
            break
    if i == len(word)-1:
        break
else:
    print("No repeated character")


# Q28. pass Inside a Loop
# Predict the output.

# for i in range(1, 4):
#     if i == 2:
#         pass
#     print(i)

# Output 

# 1 2 3

# Q29. Empty if Block
# Predict the output.

# x = 10

# if x > 5:
#     pass

# print("Finished")

# Output

# Finished


# Q30. pass in a Loop Body
# Predict the output.

# for letter in "cat":
#     pass

# print("Loop ended")

# Output

# Loop ended

# Q31. Create a Placeholder for Future Work

# Write a program with a for loop from 1 to 5. Inside the loop, use pass when the number is even. Print every number after the conditional block.

# Test cases

# Input range Expected output

# 1 to 5 1 2 3 4 5 1 to 3 1 2 3

# Explain why the even numbers are still printed.

for i in range(1,6):
    if i % 2 == 0:
        pass
    print(i)
# even numbers still be printed because pass does nothing

# Q32. Incomplete Menu Option
# Write a simple menu-like program using if / elif / else. For one option, put pass as a temporary placeholder. Print "Program closed" after the conditional structure.

# Test cases

# Choice Expected output
#    `1` The message for option 1, then `Program closed`
#    `2` No action for option 2, then `Program closed`
#    `9` The message for an unknown option, then `Program closed`
# Choose and clearly document the messages for options 1 and 9.

menu = int(input("Enter your Choice:\n\t1 ==> x\n\t2 ==> y\n\t3 ==> z\n\t4 ==> Z: "))

if menu == 1:
    print("Message")
elif menu == 2:
    pass
elif menu == 9:
    print("Unknown Option Selected")
else :
    print("Invalid input")

# Q33. Compare pass and continue
# Predict the output of each program.

# Program A

# for i in range(1, 5):
#     if i == 3:
#         pass
#     print(i)

# Output 

# 1 2 3 4


# Program B

# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)

# Output

# 1 2 4

# Explain the difference.

# Program B skips the 3rd iteration because of the continue statement in conditional if statement but since Program A has pass in its conditional if statement then it would also print 3 because pass does nothing

# Q34. Complete the Skeleton
# Fill in the blank with exactly one of break, continue, or pass so the output is 1 2 4 5.

# for i in range(1, 6):
#     if i == 3:
#         ______  # Output we will use continue in this blank because we need to print 4 and don't print 3.
#     print(i)
# Explain why the other two choices do not produce the required output.


# Q35. Output Prediction

# for i in range(1, 6):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# else:
#     print("Finished")
# Write the exact output and explain why else does or does not run.

# Output

# 1 3 Finished



# Q36. Search and Report
# Write a program that searches for a target number in a list.

# Skip negative numbers using continue.
# Stop when the target is found using break.
# Use for-else to print "Target not found" if the loop finishes without finding the target.
# Test cases

# List Target Expected output

# -2 4 7 9 7 Target found -5 -1 3 6 8 Target not found 2 4 6 2 Target found

li = [10, 1, -8, 5, -96, 52, 100, 56, -78, 0, 49, -69, 108, -62]
for i in li:
    if i < 0:
        continue
    elif i == 109:
        break
    else :
        print(i, end = " ")
else :
    print("Target not found")

# Q37. Skip, Stop, or Complete?

# Write a program that reads integers from a list in order:

# Skip 0 using continue.
# Stop before printing -1 using break.
# If the loop finishes without encountering -1, print "All values processed" using for-else.
# Test cases

# Input Expected output

# 2 0 4 -1 8 2 4 0 3 5 3 5 followed by All values processed -1 2 3 No numbers printed and no completion message

Li = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 0, 5, 4, 3, 2, -1, 0, 5, 4, 3, 2, 1, 100000]

for i in Li:
    if i == 0:
        continue
    elif i == -1:
        break
    else :
        print(i, end = " ")
else :
    print("All values processed")


# Q38. Understand Nested Loops

# Predict the output.

# for row in range(1, 4):
#     for col in range(1, 4):
#         if col == 2:
#             continue
#         if row == 3:
#             break
#         print(row, col)
#     else:
#         print("Inner loop completed")
# Answer these questions: 
# 1. Which pairs are printed?
# 1 1
# 1 3 
# Inner loop completed 
# 2 1
# 2 3 
# Inner loop completed  

# 2. Which inner loops finish without break?
# 1 & 3
 
# 3. Does the inner loop's else run for every row?
# Yes 


# Q39. Find the First Number Divisible by Both 4 and 6

# Given a list of integers, find the first number divisible by both 4 and 6. Skip negative numbers using continue. Stop when a matching number is found using break. Use for-else to report when no matching number exists.

# Test cases

# Input Expected output

# -3 8 12 24 Found: 12 5 7 10 14 No matching number -12 6 18 No matching number

LI = [1, -3, 5, -7, 9, -11, 13, -15, 17, -19, 21, -23, 25, -27, 29, -31, 33, -35, 37, -39, 41, 12, 30]

for i in LI:
    if i < 0:
        continue
    elif i == 100:
        break
    elif i % 4 ==0 and i % 6 ==0:
        print("First number divisible by 4 and 6 is:",i)
        break
else :
    print("No matching number found")

# Q40. Explain the Best Statement
# For each situation, choose the most suitable option: break, continue, for-else, or pass. Some situations may need more than one.

# Stop searching immediately after finding a username.  BREAK
# Skip a blank string and process the remaining strings. CONTINUE
# Display "Not found" only when a search loop finishes without finding a match. FOR - ELSE
# Keep an unfinished function syntactically valid while its implementation is planned. PASS
# Skip the current number but keep processing later numbers. CONTINUE
# Stop a loop when a user enters a sentinel value. BREAK
# Report that all items were checked, provided no match caused an early stop. FOR - ELSE
# Temporarily leave a conditional block empty without causing a syntax error. PASS