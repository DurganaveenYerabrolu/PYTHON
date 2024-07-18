#STRINGS:
"""strings is a sequence of characters are enclosed in single quotes '' or double quotes "". string is a collection of characters surrounded by single quotes, double quotes, or triple quotes.
they can also be createad using triple quotes which allows the string to span multiple lines.
"""
str="hai"
print(str)

firstname="hai"
lastname="dn"
print(firstname+" "+lastname)
#len
print(len(firstname))
#accessing the individual character from the string. by using loops.
for i in str:
    print(i)
i=0
while(i<len(str)):
    print(str[i],end=" ")
    i+=1
print()
#slicing strings.
name="hello world!"
print(name[:])
print(name[1:])
print(name[::-1])

#strings are the immutable sequence of characters and have a variety of built-in methods that can be used to manipulate and work with them.
#str.upper():return a new string with all the characters in the original string converted into uppercase.
print(name.upper())
#str.lower(): return a new string with all the characters in the original converted into lowercase.
print(name.lower())
#str.strip(): remove the spaces from the string.
s="haa dfnfkdf kfmklf      "
print(s.strip())
s1="hai"
s2="welcome"
#str.capitalize():return a new string with the first character of the original string can be converted into uppercase and rest of the characters converted into lowercase.
print(s.capitalize())
print(s.title())  #return a version of the string where word is titlecased.
 #convert string into lowercase.
s3=" HAi"
print(s3.lower())
print(s3.casefold())
