for i in range(1,20):
    print(i)
for i in range(20,1,-1):
    print(i)
    
name="durga naveen"
for i in range(len(name)-1,-1,-1):
    print(name[i])
#vowels and consonants in a given string
v_count=0
c_count=0
name=name.lower()
for i in name:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v_count+=1
    else:
        c_count+=1
print("no of vowels:",v_count)
print("no of consonants:",c_count)

#enter the input & how many numbers you have to compare,enter and find max number
max=0
x=int(input("enter how many number you have taken:"))
for i in range(x):
    y=int(input("enter the number:"))
    if(y>max):
        max=y
print("maximun number:",max)

#SHAPING PRINTING BY USING FOR LOOP
#square
n=int(input("enter the n:"))
for i in range(1,n+1):
    print("* "*n)
print("\n")
#Rectangle
for i in range(1,n+1):
    print("* "*(n*2))
print("\n")
#Right angle triangle
for i in range(1,n+1):
    print("* "*i)

print("\n")
#EQUILATERAL TRIANGLE
for i in range(1,n+1):
    spaces=" "*(n-i)
    stars="* "*i
    print(spaces+stars)

for i in range(n,-1,-1):
    left_spaces=" "*(n+i)
    stars=" *"*i
    print(left_spaces+stars)
#left angle triangle
for i in range(1,n+1):
    left_spaces=" "*(n-i)
    stars=" *"*i
    print(left_spaces+stars)

#prime number from one range to another range
count=0
num=23
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("prime")
else:
    print("not prime:")
#range
x=int(input("enter n1"))
y=int(input("enter n2"))
for i in range(x,y+1):
    cnt=0
    for j in range(1,i+1):
        if(i%j==0):
            cnt+=1
    if(cnt==2):
        print(i)
#PERFECT NUMBER OR NOT 6 =1+2+3(factor is equal to that number)
n1=int(input("enter the n check for perfect or not"))
sum=0
for i in range(1,n1):
    if(n1%i==0):
        sum+=i
if(sum==n1):
    print(n1,"perfect number:")
else:
    print(n1,"is not perfect number:")
#range
x1=int(input("enter the number:"))
y1=int(input("enter the 2nd num:"))
for i in range(x1,y1+1):
    sm=0
    for j in range(1,i):
        if(i%j==0):
            sm=sm+j
    if(sm==i):
        print(sum)
            
    
