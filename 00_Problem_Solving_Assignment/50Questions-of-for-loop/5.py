# 5. Sentence Word Analyzer
# Take a sentence and examine every word.

# For each word:

# Print its length.
# Print "Short" if length ≤ 3.
# Print "Medium" if length is 4–6.
# Print "Long" if length > 6.
# At the end, print the number of short, medium, and long words.


Sent=input("Enter a sentence: ").strip().split()
ct_long=0
ct_med=0
ct_short=0
for word in Sent:
    if(len(word)>6):
        print("Long")
        ct_long+=1
    elif(len(word)>3):
        print("Medium")
        ct_med+=1
    else:
        print("Short")
        ct_short+=1
print(f"The Number of long words are: {ct_long}")
print(f"The Number of medium words are: {ct_med}")
print(f"The Number of short words are: {ct_short}")