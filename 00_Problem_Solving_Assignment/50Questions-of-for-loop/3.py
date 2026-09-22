vowel=0
consonant=0
digit=0
special_character=0
vowels="aeiou"
digits="0123456789"

for i in range(1,2):
    string=input("Enter a sentence: ").lower()

    if digits in string:
        digit += 3
    elif vowels in string:
        vowel += 2
    elif "a"<string<"z":
        consonant += 1
    else :
        special_character += 4 

print("Digit score is:",digit)
print("Vowel score is:",vowel)
print("Consonant score is:",consonant)
print("Special Character score is:",special_character)
print("Total score is:",(digit+vowel+consonant+special_character))