#string handling
a = "Hello, world!"
print(a)

print(len(a)) # print the length of string, returns no. of characters in string
print(a[1]) # returns character of given index no.
print(a[2:5]) #start at 2 end at 5,but not incllude 5 
print(a.split(",")) #separates the string with given delimeter
b = "As per survey its 62 percent better with live instructor"
print(b.split(" "))

c = "  Hello  "
print(c)
print(c.strip()) #removes white spaces from start and end prefix postfix whitespaces

print(a.replace("H","Y")) #replace old char and new char
print(a.replace("o","u")) #replace old char and new char

print(a.lower()) #lowercase converts
print(a.upper()) #uppercase converts


