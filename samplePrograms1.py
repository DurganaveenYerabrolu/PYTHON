#using while loops
#factorial
fact=1
i=1
n=5
while(i<=n):
    fact=fact*i
    i+=1
print("factorial of",n,"is",fact)

i1=5
while(i1>=0):
    print(i1)
    i1-=1
#sum of natural numbers:
num=10
sum=0
i=1
while(i<=num):
    sum=sum+i
    i+=1
print("sum of",num,"is",sum)
print("\n")
#print letters in string line by line
str="hello world"
l=len(str)-1
i=0
while(i<=l):
    print(str[i])
    i+=1
    
#factors of a given number
number=34
i=1
while(i<=number):
    if number%i==0:
        print(i,end=" ")
    i+=1
print("\n")
#given number is prime or not
n2=int(input("enter the number:"))
i=1
count=0
while(i<=n2):
    if n2%i==0:
        count+=1
    i+=1
if(count==2):
    print(n2,"is a prime number:")
else:
    print(n2,"is not a prime number:")

for i in range(2,(n2//2)+1):
    if n2%i==0:
        flag=False
        print("Not Prime")
        break
    else:
        flag=True
        print("Prime")
if flag==True:
    print("prime")
else:
    print("NOT prime")
    
#REVERSE STRING
str1="hello world"
l1=len(str1)-1
while(l1>=0):
    print(str1[l1],end=" ")
    l1-=1
print("\n")
#STRING PALINDROME
name="maggam"
rev=""
length=len(name)-1
while(length>=0):
    rev=rev+name[length]
    length-=1
print(rev)
if(name==rev):
    print("It is a String Palondrome:")
else:
    print("it is not a String Palindrome:")
    
    
