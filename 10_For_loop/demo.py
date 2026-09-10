
i=int(input("ENTER A THREE DIGIT NUMBER:"))
one=i//10
two=one//10
print(f"Sum of digits is: {i%10 + one%10 + two%10}")
num=int(input("Enter a number:"))
for i in range(num,num+11):
    if i%2==0:
        print(f"{i} is even !!!!!!!")