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