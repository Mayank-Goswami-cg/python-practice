fail_count = 0
pass_count = 0
good_count = 0
excellent_count = 0

for i in range(1, 11):
    marks = float(input(f"Enter marks for student {i}: "))
    
    if marks < 35:
        print("Fail")
        fail_count += 1
    elif 35 <= marks <= 49:
        print("Pass")
        pass_count += 1
    elif 50 <= marks <= 74:
        print("Good")
        good_count += 1
    elif 75 <= marks <= 100:
        print("Excellent")
        excellent_count += 1

print("Performance Summary:")
print("Fail",fail_count)
print("Pass:", pass_count)
print("Good:", good_count)
print("Excellent:", excellent_count)