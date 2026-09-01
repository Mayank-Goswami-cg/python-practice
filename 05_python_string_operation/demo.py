#Indexing
#PYTHON
#012345
#-6,-5,-4,-3,-2,-1

b="Python"
print(b[5], b[-5])

# == (comparision operator) output in boolean

a="Python"
print(a==b)

#Line break through Triple qoutes and \n

print("""Dear Sir,
       Good Morning.""")

print("Dear Ma'am, \n       Good Morning.")


#Sting Slicing

print(b[5])    #print(b[starting point : ending point]) 
print(b[0:5])  #if you want to end in 5 you have to set end point 6 because it gets sliced
print(b[:6])
print(b[:])

#Reversing A String

print(b[::1])
print(b[::-1])

#Searching in strings

message="Hello, Mayank"
print("Mayank" in message)
print("Python" not in message)
print(message.find("Java"))
print(message.find("Mayank"))
text="banananananananana"
b=text.count("a")
print(b)
print(text.count("z"))
print(message.startswith("Hello"))
print(message.endswith("k"))


#Replacing text
Shlok="Darsh is my best friend."
print(Shlok,"To -->",Shlok.replace("friend", "Brother"))

# 1/09/26

a="Hello, Python"
b="pyTHon"
c=b.lower() in a.lower()
print(c)
print("Hello\nWorld")
print("Hello\tMAYAnk")

#Raw String
path= r"C:\newfolder\newfile.html"
print(path)
