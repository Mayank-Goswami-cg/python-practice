#3.
Str=input("Write a sentence: ").strip().lower().split()
point=0
for word in Str[0:1]:
    for char in word:
        if(char=='a'or char=='i'or char=='e' or char=='o' or char=='u'):
            point+=2
        elif(char>='0' and char<='9'):
            point+=3
        elif(char>='a' and char<='z'):
            point+=1
        else:
            point+=4
    high=point
    x=Str[0]
        
i=0
for word in Str[1:]:
    point=0
    for char in word:
        if(char=='a'or char=='i'or char=='e' or char=='o' or char=='u'):
            point+=2
        elif(char>='0' and char<='9'):
            point+=3
        elif(char>='a' and char<='z'):
            point+=1
        else:
            point+=4
    i+=1
    if(point>high):
        high=point
        x=Str[i]
print("The word with the highest points is :",x)
print("The points are: ",high)




